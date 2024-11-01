from sqlalchemy.orm import Session
from database.models import User
from datetime import datetime

def create_user(db: Session, user_id: int, user_name: str, full_name: str, owner_id: int):
    user = User(
        user_id=user_id,
        user_name=user_name,
        full_name=full_name,
        owner_id=owner_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def update_user(db: Session, user_id: int, balance: float = None, energy_count: int = None, refferals_count: int = None):
    user = db.query(User).filter(User.user_id == user_id).first()

    if balance is not None:
        user.balance = balance
    if energy_count is not None:
        user.energy_count = energy_count
    if refferals_count is not None:
        user.refferals_count = refferals_count
    
    db.commit()
    db.refresh(user)
    db.close()
    return user
