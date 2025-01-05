import requests

# Define the API endpoint and request payload
url = "http://127.0.0.1:8000/analyze-trends/"
payload = {
    "spending_trend": "Food, Entertainment, Travel, Utilities",
    "pre_saving_goal": "5000",
    "budget": 30000
}

# Make the POST request
response = requests.post(url, json=payload)

# Check and print the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
