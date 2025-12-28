UrbanGuard-XAI: Agentic Explainability for Spatiotemporal Graphs 🤖🌆
📖 Overview
UrbanGuard-XAI is an interpretability layer designed to solve the "Black Box" problem in urban traffic forecasting. While state-of-the-art models like T-GCN provide high-accuracy predictions, they often lack the transparency required for critical urban decision-making.

This project introduces an AI Agent that performs heuristic analysis on GNN embeddings to provide natural language diagnostics, turning raw traffic forecasts into actionable situational reports for urban planners.

✨ Key Features
Agentic Reasoning: Utilizes LLM agents (LangChain/GPT-4o) to interpret the hidden states of graph neural networks.

Spatiotemporal Heuristics: Analyzes "ripple effects" in traffic propagation across the Nanshan District road network.

Natural Language Diagnostics: Generates human-readable explanations (e.g., "Congestion predicted at Node 42 due to downstream bottleneck at Intersection B").

Research Integration: Built to work seamlessly with my Traffic-GNN-Shenzhen predictive engine.

🛠️ Architecture
UrbanGuard operates as the Intelligence Layer in a dual-layer urban system:

The Engine (T-GCN): Predicts future traffic flow based on historical SZ-taxi data.

The Guardian (UrbanGuard): Analyzes the GNN’s attention weights and node importance to explain why the prediction was made.

🚀 Getting Started
Prerequisites
Python 3.9+

PyTorch & PyTorch Geometric

OpenAI API Key (for Agentic Reasoning)

Installation
Bash

git clone https://github.com/zolaray/UrbanGuard-XAI.git
cd UrbanGuard-XAI
pip install -r requirements.txt
📂 Repository Structure
Plaintext

├── agents/             # LLM Agent orchestration logic
├── xai_engine/         # GNN feature extraction & attention analysis
├── data/               # Processed SZ-taxi dataset samples
├── notebooks/          # Demonstration of reasoning traces
└── README.md
📑 Research Context
This project is part of my proposed Master’s research on Trustworthy Spatiotemporal Intelligence. It bridges the gap between high-performance deep learning and the interpretability needed for real-world smart city deployment.

Contact: zolarayanwork@gmail.com
