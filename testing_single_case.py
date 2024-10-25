import requests

test_case = {
    "text": "Scientists confirm that the Earth is actually flat and not round.", 
    "expected": 1 
}

url = "http://serve-sentiment-env.eba-gt2b3ixf.us-east-2.elasticbeanstalk.com/predict"

try:
    response = requests.post(url, json={"text": test_case["text"]})
    if response.status_code == 200:
        result = response.json().get("prediction")
        if result == test_case["expected"]:
            print("Test passed.")
        else:
            print(f"Test failed: expected {test_case['expected']} but got {result}.")
    else:
        print(f"Test failed with status code {response.status_code}")
        print("Response text:", response.text)
except requests.exceptions.RequestException as e:
    print(f"Test encountered an error: {e}")
