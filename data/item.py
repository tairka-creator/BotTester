from dataclasses import dataclass

@dataclass
class Item:
    id: int
    price: int


subscribe = Item(id=1, price=1)

items = [subscribe]