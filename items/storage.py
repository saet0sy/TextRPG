from dataclasses import dataclass

from items.item import Item

@dataclass
class Storage:
    items: list[Item]