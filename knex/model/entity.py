from pydantic import BaseModel

class Entity(BaseModel):
    """
    Represents a unique entity. It has a key, a class and a label.
    The label is the one that will be used to display the entity.
    """

    pk_entity: int
    pk_class: int
    label: str

    def __init__(self, pk_entity: int, pk_class: int, label: str):
        self.pk_entity = pk_entity
        self.pk_class = pk_class
        self.label = label
