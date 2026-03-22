# Expense Tracking App

A simple FastAPI app for managing wallet balances and tracking expenses.

## What it does

The app lets you:
- Check the total balance across all wallets
- Check the balance of a specific wallet
- (Coming soon: add expenses, top up balances, etc.)

## How to run

1. Install the required packages:
   ```
   pip install fastapi uvicorn
   ```

2. Start the server:
   ```
   uvicorn main:app --reload
   ```

3. Open your browser to http://127.0.0.1:8000/docs for the API documentation.

## API Endpoints

- `GET /balance` - Get total balance or a specific wallet's balance
  - Optional query parameter: `wallet_name`

## Project files

- `main.py` - The main app file