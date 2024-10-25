import requests
import time
import csv

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
url = "http://serve-sentiment-env.eba-gt2b3ixf.us-east-2.elasticbeanstalk.com/predict"

with open("latency_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Test Case", "Request Number", "Response Time (ms)"])

    for case_num, test in enumerate(test_cases, 1):
        for i in range(100):
            start_time = time.time()
            response = requests.post(url, json={"text": test["text"]})
            end_time = time.time()

            # Calculate response time in milliseconds
            response_time = (end_time - start_time) * 1000
            writer.writerow([f"Case {case_num}", i + 1, response_time])