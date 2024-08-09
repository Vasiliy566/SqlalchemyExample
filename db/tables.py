from sqlalchemy import Column, Integer, String

from db.base import Base


class Router(Base):
    __tablename__ = 'routers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
    amount = Column(Integer)

    def __repr__(self):
        return f"{self.id}: {self.name} {self.cost} {self.amount}."