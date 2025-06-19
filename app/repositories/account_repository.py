from sqlalchemy.orm import Session
from app.models.account.account import Account
from app.repositories.entities.account.account_id_entity import AccountIdEntity
#from app.repositories.entities.account.account_transaction_entity import AccountTransactionEntity
from fastapi import HTTPException, status
from app.models.account.account_transaction import AccountTransaction
from typing import List

def get_account(id_account: int, db: Session) -> Account:
    account = db.query(AccountIdEntity).filter(AccountIdEntity.id_account == id_account).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account with ID {id_account} not found"
        )
    return account

# def get_transactions(id_account: int, db: Session) -> List[AccountTransaction]:
#     transactions = (
#         db.query(AccountTransactionEntity)
#         .filter(AccountTransactionEntity.id_account == id_account)
#         .all()
#     )

#     return [
#         AccountTransaction.model_validate(txn, from_attributes=True)
#         for txn in transactions
#     ]