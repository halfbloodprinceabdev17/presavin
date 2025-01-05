from fastapi import FastAPI, HTTPException
import yfinance as yf
import pandas as pd
import os
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Define the endpoint to search for stock data
@app.get("/search/{stock_name}")
async def search_stock(stock_name: str):
    if not stock_name:
        raise HTTPException(status_code=400, detail="Stock name cannot be empty")

    try:
        # Fetch stock data using yfinance
        stock = yf.Ticker(stock_name)
        stock_info = stock.info
        hist_1y = stock.history(period="1y")

        # Get the current price with fallback
        current_price = (
            stock_info.get("currentPrice")
            or stock_info.get("lastPrice")
            or stock_info.get("previousClose")
            or stock_info.get("regularMarketPrice")
            or "Data not available"
        )

        # Calculate 1-year growth rate
        def calculate_growth(data):
            if data.empty:
                return "Data not available"
            start_price = data['Close'].iloc[0]
            end_price = data['Close'].iloc[-1]
            return round(((end_price - start_price) / start_price) * 100, 2)

        growth_1y = calculate_growth(hist_1y)

        # Prepare response data
        response_data = {
            "stock_info": {
                "current_price": current_price,
                "name": stock_info.get("shortName", "N/A"),
                "symbol": stock_info.get("symbol", stock_name),
                "growth_rates": {
                    "1_year": f"{growth_1y}%"
                }
            }
        }

        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Run the app with uvicorn when executed
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)
