import requests

# Define the test cases
test_cases = [
    #fake news
    {"text": "Scientists confirm that the Earth is actually flat and not round.", "expected": 1},
    {"text": "Eating chocolate every day has been proven to double your lifespan.", "expected": 1},
    #real news
    {"text": "Toronto city council approved new measures to improve public transportation.", "expected": 0},
    {"text": "Justin trudeau is the Prime Minister of Canada.", "expected": 0}
]

# URL for the deployed API (replace with your AWS Elastic Beanstalk endpoint)
url = "http://127.0.0.1:5000/predict"

# Run each test case
for i, test in enumerate(test_cases, 1):
    try:
        response = requests.post(url, json={"text": test["text"]})
        if response.status_code == 200:
            result = response.json().get("prediction")
            if result == test["expected"]:
                print(f"Test case {i} passed.")
            else:
                print(f"Test case {i} failed: expected {test['expected']} but got {result}.")
        else:
            print(f"Test case {i} failed with status code {response.status_code}")
            print("Response text:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Test case {i} encountered an error: {e}")