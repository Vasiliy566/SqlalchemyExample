import random

from db.base import session_maker
from db.tables import Router

session = session_maker()


def create_router(name: str, cost: int, amount: int):
    session.add(
        Router(id=random.randint(0, 10000), name=name, cost=cost, amount=amount)
    )
    session.commit()


def get_all_routers():
    return session.query(Router).all()


def get_router(router_id: int):
    return session.query(Router).filter(Router.id == router_id).first()


def update_router_amount(name: str, amount: int):
    router = session.query(Router).filter(Router.name == name).first()
    router.amount += amount
    session.commit()


def delete_router(router_id):
    router = session.query(Router).filter(Router.id == router_id).first()
    session.delete(router)
    session.commit()


if __name__ == "__main__":
    create_router("Test1", 1000, 5)
    create_router("Test2", 5000, 0)
    create_router("Test3", 2000, 2)
    create_router("Test4", 3000, 1)
