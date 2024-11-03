# INTERVIEW TEST PYTHON CODE

## Introduction
This project consists of two different sub-projects. A REST API project based on Flask and a data processing project based on statistical approaches. 
The aim of this project is to evaluate the condidat's ability to develop REST API applications. But also to analize the data thus provided.

Here are the three tasks in this project
- _*TASK 1 - DATA INGESTION & PROCESSING*_
- _*TASK 2 - BASIC REST API DEVELOPMENT*_
- _*TASK 3 - SIMPLE DATA ANALYTICS*_

## Get the project
To get the project's dependencies, you need to have ```poetry 1.8.4```  or later installed.

_Clone the project and install all dependencies_:
``` 
> git clone https://github.com/Rasoavelonirina/dakicartons_interview_test_python.git
> cd dakicartons_interview_test_python
> poetry install
``` 
_Then activate the virtual environment to make sure the codes are working properly_:
```
> poetry shell
```

## TASK 1 - DATA INGESTION & PROCESSING
### Description:
Write a Python script that reads a continuous stream of simulated machine data (e.g., temperature, speed, and status). The script should:
-	Read the data every 10 seconds from a JSON file or a mocked endpoint.
-	Transform the data to calculate a moving average for each parameter over the last 5 readings.
-	Print the transformed data in JSON format

### Results:
After activating the appropriate virtual env with the ```poetry shell``` command. Run the calculation script as follows:
```
python data_processing/moving_average.py
```
This one will generate a loop error because the data it needs is provided by the **TASK 2 - BASIC REST API DEVELOPMENT**.
```
Error fetching data: HTTPConnectionPool(host='127.0.0.1', port=5000): Max ...
```
If the **TASK 2 - BASIC REST API DEVELOPMENT** is operational, the expected results should look like this:
```
{
    "average_temperature": 20.18,
    "average_speed": 899.64,
    "status": "IDLE"
}
```

## TASK 2 - BASIC REST API DEVELOPMENT
### Description:
Build a simple REST API using Flask that expose 2 endpoints: 
-	[GET]: /data returns the processed machine data as JSON
-	[POST]: /status allows updating machine’s job status (e.g. “STARTED”, “COMPLETED”)
### Results:
Run the following command to start the API:
```
> python machine_status_api/main.py
```
Subsequently, the flask API will have to launch and wait for requests on the following link ```http://127.0.0.1:5000```
You can use any api query application to test its functionality


#### GET (to get some data information from the API)
Use the ```http://127.0.0.1:5000/data``` link to obtain simulated data as follows:
```
{
    "description": "Machine for processing ",
    "fan_speed": 811.62,
    "id": 1,
    "name": "DELL G450",
    "status": "COMPLETED",
    "temperature": 30.21,
    "timestamp": "2024-11-03T13:40:45.015069+00:00"
}
```


#### POST (allows updating machine’s job status)
Use the ```http://127.0.0.1:5000/status``` link to update machine’s job status:

e.g: Updating machine’s job status to **COMPLETED**, you need to POST ```{"status": "COMPLETED"}``` as data to the link ```http://127.0.0.1:5000/status```. Then as result, you will get this message:
```
{
    "message": "Status updated"
}
```

**error message**:
- Not allowed status:
```
{
    "error": "Invalid status. Allowed statuses: STARTED, ERROR, IDLE, COMPLETED"
}
```
- Status fields not filled in or missing:
```
{
    "error": "Missing 'status' field in request data"
}
```

## TASK 3 - SIMPLE DATA ANALYTICS
### Description
Implement a Python function that reads a list of timestamps and values (e.g. machine speed) and calculates: 
-	The average value over the entire period
-	The maximum and minimum values	

Bonus: If the candidate has time, they can extend the function to detect if there is an anomaly (e.g., if any value deviates by more than 20% from the average)

### Results:
The definition of the function satisfying this task is located in the file ```dakricartons/utils.py```. Here is the function header:

```
def analyze_values(data: List[Tuple[str, float]], anomaly_threshold: float = 0.2) -> Dict:
    '''
    Analyzes a list of timestamps and values (e.g., machine speed).
    
    Parameters:
    - data: A list of tuples where each tuple contains a timestamp (str) and a value (float).
    - anomaly_threshold: The deviation threshold for anomaly detection, default is 20%.
    
    Returns:
    - A dictionary with average, max, min values, and a list of anomalies.
    '''
```

To test it, you can launch the script:
```
python -m tests.test_average
```
As a result, it will return something like this:
```
{
    "average": 105.83333333333333,
    "max": 130,
    "min": 80,
    "anomalies": [
        {
            "timestamp": "2023-11-01T10:30:00",
            "value": 130,
            "deviation": 24.16666666666667
        },
        {
            "timestamp": "2023-11-01T10:50:00",
            "value": 80,
            "deviation": 25.83333333333333
        }
    ]
}
```