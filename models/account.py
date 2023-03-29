from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, backref
from models.base import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    balance = Column(Integer)

    positions = relationship('Position', back_populates='account')


    def __init__(self, id, balance):
        self.id = id
        self.balance = balance