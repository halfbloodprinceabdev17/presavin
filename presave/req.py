import requests
import tkinter as tk
from tkinter import ttk
import json

from flask import Flask, jsonify


import firebase_admin
from firebase_admin import credentials, firestore


# Initialize Firebase Admin SDK (Ensure the service account key is provided)
if not firebase_admin._apps:
    cred = credentials.Certificate("personal-finance-app-650d0-firebase-adminsdk-n3err-78f92ac6e4.json")  # Update this path
    firebase_admin.initialize_app(cred)


def fetch_historical_data(user_id):

    # Get Firestore client
    db = firestore.client()

    # Year to analyze
    year = 2024

    # Dictionary to store expenses categorized by month
    historical_data = {}

    try:
        # Reference to the user's expense collection for the year 2024
        year_ref = db.collection("users").document(user_id).collection("expense").document(str(year))

        # Loop through each month (1 to 12)
        for month in range(1, 13):
            month_ref = year_ref.collection(str(month))

            # Fetch all documents for the current month
            docs = month_ref.stream()

            for doc in docs:
                data = doc.to_dict()
                category = data.get("category", "Uncategorized")  # Default to "Uncategorized" if missing
                amount = data.get("amount", 0.0)  # Default to 0.0 if amount is missing

                # Ensure the category exists in the dictionary
                if category not in historical_data:
                    historical_data[category] = [0.0] * 12  # Initialize with zeros for 12 months

                # Add the amount to the correct month (index is month - 1)
                historical_data[category][month - 1] += amount

        # Print the historical data for verification
        print("Historical Data:")
        for category, totals in historical_data.items():
            print(f"Category: {category}, Monthly Totals: {totals}")

        return historical_data

    except Exception as e:
        print(f"Error fetching historical data: {e}")
        return {}

def convert_to_key_value_pairs(data):
  
    return {category: sum(values) for category, values in data.items()}

app = Flask(__name__)

@app.route('/data')
def json_data():
        
    url = "http://127.0.0.1:8000/analyze-trends/"
    user_id = "5gok8ctNtJgil7RtG1VYQpaRWaf2"
    historical_data = fetch_historical_data(user_id)
    converted_data = convert_to_key_value_pairs(historical_data)
    data1 = str(converted_data)
    data = {
        "spending_trend":data1,
        "pre_saving_goal": "125",
        "budget": 4000
    }
    
  
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)


# Data
    data1 = response.json()
    data31 = str(data1["table"])
    new_data = data31.replace("\n","")
    new_data1 = new_data.replace("```","")
    new_data2 = new_data1.replace("json","")
    new_json_data = json.loads(new_data2)
    

    return jsonify(new_json_data)

if __name__ =="__main__":
    app.run()

