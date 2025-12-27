import random

def generate_situational_report(node_id: int, timestamp: str, predicted: int, actual: int):
    """
    Generates a situational report for a traffic anomaly.
    In a real implementation, this function would query an LLM.
    """
    
    # 1. Format the input for the LLM agent
    error_percentage = ((actual - predicted) / predicted) * 100
    input_to_llm = f"At Node {node_id} at {timestamp}, the model predicted {predicted} vehicles, but {actual} were observed."

    # 2. Placeholder for the actual LLM call
    # -------------------------------------------------------------------
    # In a real application, you would use a library like openai,
    # langchain, or a direct API call to send the `input_to_llm`
    # to a powerful model and get a generated explanation.
    #
    # Example (using a hypothetical 'llm' library):
    #
    # prompt = f"""
    # You are a traffic analysis expert for the city of Shenzhen.
    # Your task is to provide a brief, insightful explanation for a traffic anomaly detected by a T-GCN model.
    # Use the following data to generate your report:
    #
    # ANOMALY DATA:
    # {input_to_llm}
    #
    # ANALYSIS INSTRUCTIONS:
    # - Start by stating the severity of the anomaly (e.g., "Minor discrepancy," "Significant spike," "Major anomaly detected").
    # - Hypothesize a likely cause (e.g., "localized event," "sensor malfunction," "unexpected road closure," "spillover from a nearby event").
    # - If possible, suggest correlations with other nodes (you may need to provide more context for this).
    # - Keep the report concise (2-3 sentences).
    #
    # SITUATIONAL REPORT:
    # """
    # explanation = llm.generate(prompt)
    # -------------------------------------------------------------------

    # 3. For this demo, we return a hardcoded, dynamic template
    severity = "Anomaly"
    if error_percentage > 100:
        severity = "Critical Anomaly"
    elif error_percentage > 50:
        severity = "Significant Spike"
        
    causes = ["a localized event (like a minor accident or a delivery truck blocking a lane)", "unexpected congestion due to a nearby road closure", "a public event in the vicinity", "sensor noise or a temporary sensor malfunction"]
    chosen_cause = random.choice(causes)
    
    explanation = f"{severity} detected at Node {node_id}. The {error_percentage:.0f}% spike above the predicted flow suggests {chosen_cause}. The T-GCN model's spatial analysis should be reviewed to see if this is impacting adjacent nodes."

    return input_to_llm, explanation
