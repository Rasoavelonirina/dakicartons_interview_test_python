from typing import List, Tuple, Dict

def analyze_values(data: List[Tuple[str, float]], anomaly_threshold: float = 0.2) -> Dict:
    """
    Analyzes a list of timestamps and values (e.g., machine speed).
    
    Parameters:
    - data: A list of tuples where each tuple contains a timestamp (str) and a value (float).
    - anomaly_threshold: The deviation threshold for anomaly detection, default is 20%.
    
    Returns:
    - A dictionary with average, max, min values, and a list of anomalies.
    """
    
    if not data:
        return {
            "average": 0,
            "max": None,
            "min": None,
            "anomalies": []
        }
    
    # Extract just the values for easier calculation
    values = [value for _, value in data]

    # Calculate average, max, and min
    avg_value = sum(values) / len(values)
    max_value = max(values)
    min_value = min(values)

    # Anomaly detection
    anomalies = [
        {"timestamp": timestamp, "value": value, "deviation": abs(value - avg_value)}
        for timestamp, value in data
        if abs(value - avg_value) > anomaly_threshold * avg_value
    ]

    # Results dictionary
    return {
        "average": avg_value,
        "max": max_value,
        "min": min_value,
        "anomalies": anomalies
    }

