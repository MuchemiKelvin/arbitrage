
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Float, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

class Price(Base):
    __tablename__ = 'prices'
    id = Column(Integer, primary_key=True)
    exchange = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_price_to_db(exchange, symbol, price):
    new_price = Price(exchange=exchange, symbol=symbol, price=price)
    session.add(new_price)
    session.commit()
        