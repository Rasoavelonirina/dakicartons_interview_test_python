from dakricartons import utils
import json

# Run the data processing function
if __name__ == "__main__":
    # Example usage
    data = [
        ("2023-11-01T10:00:00", 100),
        ("2023-11-01T10:10:00", 120),
        ("2023-11-01T10:20:00", 90),
        ("2023-11-01T10:30:00", 130), # Anomalous value
        ("2023-11-01T10:40:00", 115),
        ("2023-11-01T10:50:00", 80),  # Anomalous value
    ]

    result = utils.analyze_values(data)
    print(json.dumps(result, indent=4))