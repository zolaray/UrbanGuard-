import streamlit as st
import pandas as pd
import pydeck as pdk

# Import the explainer function
from explainer import generate_situational_report

# --- App Configuration ---
st.set_page_config(
    page_title="UrbanGuard: Shenzhen Traffic Analysis",
    page_icon="🚦",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data
def load_data(filepath):
    """Loads the traffic prediction data and converts timestamp."""
    data = pd.read_csv(filepath)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data

try:
    df = load_data("predictions.csv")
except FileNotFoundError:
    st.error("Error: `predictions.csv` not found. Make sure the file is in the `UrbanGuard` directory.")
    st.stop()

# --- Sidebar Controls ---
st.sidebar.title("UrbanGuard Controls")
st.sidebar.markdown("Select a traffic node to inspect its data and generate an AI-powered situational report.")

# Use the unique nodes from the dataframe for the selection
node_list = df['node_id'].unique()
selected_node = st.sidebar.selectbox(
    "Select a Node ID",
    node_list
)

# --- Main Dashboard ---
st.title(f"🚦 UrbanGuard: Traffic Analysis for Node {selected_node}")

# Filter data for the selected node
node_data = df[df['node_id'] == selected_node].set_index('timestamp')

# --- Map Visualization ---
st.subheader("Shenzhen Node Map")

# Get unique nodes for map display
map_data = df[['node_id', 'lat', 'lon']].drop_duplicates()

# Highlight the selected node
map_data['color'] = map_data.apply(lambda row: [255, 0, 0, 200] if row['node_id'] == selected_node else [0, 128, 255, 150], axis=1)
map_data['size'] = map_data.apply(lambda row: 150 if row['node_id'] == selected_node else 100, axis=1)


# Set the initial view state for the map
view_state = pdk.ViewState(
    latitude=map_data['lat'].mean(),
    longitude=map_data['lon'].mean(),
    zoom=12,
    pitch=50
)

# Define the scatter plot layer for the map
layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_data,
    get_position='[lon, lat]',
    get_color='color',
    get_radius='size',
    pickable=True,
    tooltip={"text": "Node ID: {node_id}"}
)

# Render the map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=view_state,
    layers=[layer]
))


# --- Traffic Flow Chart ---
st.subheader("Predicted vs. Actual Traffic Flow")
st.line_chart(node_data[['predicted', 'actual']])


# --- Agentic Explainer Section ---
st.subheader("🤖 AI-Powered Situational Report")

# Find the point with the biggest anomaly
node_data['error'] = (node_data['actual'] - node_data['predicted']).abs()
anomaly = node_data.loc[node_data['error'].idxmax()]

# Generate and display the report
input_prompt, explanation = generate_situational_report(
    node_id=selected_node,
    timestamp=anomaly.name.strftime('%Y-%m-%d %H:%M:%S'),
    predicted=int(anomaly['predicted']),
    actual=int(anomaly['actual'])
)

with st.container(border=True):
    st.markdown("**Anomaly Input:**")
    st.text(input_prompt)
    st.markdown("**LLM Agent Output:**")
    st.info(explanation)
