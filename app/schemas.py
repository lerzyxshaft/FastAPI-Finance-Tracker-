from pydantic import BaseModel, Field, field_validator

class OperationRequest(BaseModel):
    name: str = Field(..., max_length=127)
    amount: float
    initial_balance: float = 0

    @field_validator("amount")
    def amount_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

    @field_validator("wallet_name")
    def wallet_name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v :
            raise ValueError("Wallet name ")
        return v

    @field_validator("initial_balance")
    def balance_not_negative(cls, v: float) -> float:

        if v < 0:
            raise ValueError("Initial balance cannot be negative")
        return v
    
class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=127)
    initial_balance: float = 0

    @field_validator("name")
    def name_is_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet cannot be empty")
        return v
    
    @field_validator("initial_balance")
    def balance_not_negative(cls, v:float) -> float:
        if v < 0:
            raise ValueError("Initial balance cannot be negative")
        return v