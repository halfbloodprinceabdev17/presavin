from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from groq import Groq
import ast
# Initialize FastAPI
app = FastAPI()

# Configure Groq client
groq_client = Groq(api_key="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")

# Request Model
class SpendingTrendRequest(BaseModel):
    spending_trend: str
    pre_saving_goal: str  # Pre-saving goal is optional
    budget: Optional[float] = None

# Helper function to format output as a table
def format_as_table(response_text: str) -> List[Dict[str, str]]:
    """
    Parse the response text into a structured table format.
    Each row includes 'Category', 'Suggestion', and 'Notes'.
    """
    table = []
    rp = response_text.replace("*","")
    rows = rp.split("\n")
    for row in rows:
        if ":" in row:
            parts = row.split(":", 1)
            category = parts[0].strip()
            suggestion = parts[1].strip()
            notes = "Consider this suggestion based on your spending trend." if "consider" in suggestion.lower() else ""
            table.append({"Category": category, "Suggestion": suggestion, "Notes": notes})
    return rp

# Helper function to interact with Groq
def analyze_trends_with_groq(spending_trend: str, budget: Optional[float], pre_saving_goal: str) -> List[Dict[str, str]]:
    # Prepare the system and user messages for Groq
    system_prompt = (
        """
    You are a financial assistant tasked with analyzing spending trends and providing a personalized budget analysis. If a pre-saving goal is provided, include detailed suggestions on how to achieve it.

**Instructions:**
- Only respond with JSON, nothing extra.
- If a pre-saving goal is provided, calculate the EMI (Equated Monthly Installment) based on the time span and divide the total savings goal by the EMI.
- Ensure that the total reduced amount across different categories sums up to match the EMI exactly.
- For each category, provide an exact amount of money to be reduced, followed by the percentage of the total budget that it represents.
- Provide a detailed budget analysis, including categories, suggestions, and any additional notes.
- reduce budget according to the calculated monthly emi which is pre-saving goal/timespan
- everything should be in indian rupees, use INR instead of $
- Always format the response as follows:


{
    "budget_analysis": [
        {
            "Category": "Category Name",
            "Notes": "Any additional notes on the category",
            "Suggestion": "Reduce spending by Amount INR (Percentage%)"
        },
        {
            "Category": "Category Name",
            "Notes": "Any additional notes on the category",
            "Suggestion": "Reduce spending by Amount INR (Percentage%)"
        },
        {
            "Category": "Category Name",
            "Notes": "Any additional notes on the category",
            "Suggestion": "Reduce spending by Amount  INR (Percentage%)"
        }
    ],
    "summary": {
        "monthly_savings_emi": "Amount INR",
        "time_span": "Time in months",
        "total_savings_goal": "Amount INR"
    }
}
    - keep in mind "monthly_savings_emi"[Amount] = all Category[Amount] summed up

 """
    )
    user_message = f"""
    Spending Trend: {spending_trend}
    Budget: {budget if budget is not None else "Not Provided"} INR per month
    reduce : {pre_saving_goal if pre_saving_goal is not None else "Not Provided"} this amount for the spendings
    only use catagories in the spending trend do not add anything on your own
    Provide a tabular analysis with columns: Category, Suggestion, and Notes.
    """
    print(user_message)
    try:
        # Send the request to Groq LLM
        chat_completion1 = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            model="llama-3.1-70b-versatile",
        )

        # Extract the response text
        #print(chat_completion.choices)
        #
        response_text = chat_completion1.choices[0].message.content
        response_text_string = str(response_text)
     

        return format_as_table(response_text_string)  # Format response as table
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API  error: {str(e)}")


# API endpoint
@app.post("/analyze-trends/")
async def analyze_spending_trend(request: SpendingTrendRequest):
    try:
        table_data = analyze_trends_with_groq(
            spending_trend=request.spending_trend,
            budget=request.budget,
            pre_saving_goal=request.pre_saving_goal,
        )
        return {"table": table_data}
    except HTTPException as e:
        return {"error": e.detail}
