from fastapi import HTTPException

from app.schemas import OperationRequest
from app.repository import wallets as wallets_repository

def add_income(operation: OperationRequest)
    if wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{operation.wallet_name}' is not found"
        )
    
    new_balance = wallets_repository.add_income(operation.wallet_name, operation.add_income )

    return {
        "message": "Income added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance":new_balance
    }

def add_expense(operation: OperationRequest)
    if wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code = 404, 
            detail=f"Wallet {operation.wallet_name}' is not found"
        )
    
    if operation.amount <= 0:
        raise HTTPException(
            status_code=404,
            detail=f"Amount must be positive"
        )
    
    if BALANCE[operation.wallet_name] < operation.amount:
        raise HTTPException(
            status_code = 404,
            detail = f"Insufficient founds. Available {BALANCE[operation.wallet_name]} "
        )
    
    BALANCE[operation.wallet_name] -= operation.amount

    return {
        "message": "Expense added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": BALANCE[operation.wallet_name]
    }