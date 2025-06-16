from sqlalchemy.orm import Session
from app.models.account.account import Account
from app.repositories.entities.account.account import AccountIdEntity
from fastapi import HTTPException, status

def get_account(id_account: int, db: Session) -> Account:
    account = db.query(AccountIdEntity).filter(AccountIdEntity.id_account == id_account).first()
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account with ID {id_account} not found"
        )
    return account