def get_wallet(wallet_name: str | None):
    if wallet_name is None:
        return {"total_balance": sum(BALANCE.values())}
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' is not found"
        )
    
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}

def create_wallet(wallet: CreateWalletRequest):
    if wallet.name in BALANCE:
        raise HTTPException(
            status_code=400,
            detail=f"Wallet '{wallet.name}' already exists"
        )

    BALANCE[wallet.name] = wallet.initial_balance
    return {
        "message": f"Wallet '{wallet.name}' created",
        "wallet": wallet.name,
        "balance": BALANCE[wallet.name]
    }