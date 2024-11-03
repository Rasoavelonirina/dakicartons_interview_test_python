from collections import deque
from statistics import mean
from typing import Dict
import json
import time
import requests

ENDPOINT_URL = "http://127.0.0.1:5000/data"

# Initialize deque to store the last 5 readings for each parameter
temperature_readings = deque(maxlen=5)
speed_readings = deque(maxlen=5)
status_readings = deque(maxlen=5)

# Function to calculate moving average
def calculate_moving_average(readings: deque) -> float:
    return mean(readings) if readings else 0.0

# Function to fetch data from the endpoint
def fetch_data_from_endpoint(url: str) -> Dict:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}  # Return empty dictionary if there's an error

# Main function to process data
def process_data(url: str):
    while True:
        # Fetch data from the endpoint
        data = fetch_data_from_endpoint(url)
        
        if data:
            # Extract parameters
            temperature = data.get("temperature", 0)
            speed = data.get("fan_speed", 0)
            status = data.get("status", "IDLE")
            
            # Add new readings to deques
            temperature_readings.append(temperature)
            speed_readings.append(speed)
            status_readings.append(status)
            
            # Calculate moving averages for temperature and speed
            avg_temperature = calculate_moving_average(temperature_readings)
            avg_speed = calculate_moving_average(speed_readings)

            # Prepare transformed data
            transformed_data = {
                "average_temperature": avg_temperature,
                "average_speed": avg_speed,
                "status": status  # Latest status
            }

            # Print transformed data in JSON format
            print(json.dumps(transformed_data, indent=4))
        
        # Wait 10 seconds before the next reading
        time.sleep(10)

# Run the data processing function
if __name__ == "__main__":
    process_data(ENDPOINT_URL)
