import random
import string
import time
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Float,Boolean,BigInteger,TIMESTAMP
from database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    registeredAt = Column(BigInteger,default=int(time.time()))
    user_id = Column(BigInteger)
    user_name = Column(String)
    full_name = Column(String)
    balance = Column(Float,default=0.0)
    energy_count = Column(Integer,default=0)
    owner_id = Column(BigInteger)
    refferals_count = Column(Integer,default=0)
    refferals_deposit_count = Column(Integer,default=0)
    refferals_earned = Column(Integer,default=0)
    refferals_percent = Column(Integer,default=30)



    