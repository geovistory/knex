from pydantic import BaseModel


class Triple(BaseModel):
    """
    Represent an ontological triple: subject - property - object.
    An object can either be an entity (int), or a value (tuple or string).
    """

    subject: int
    property: int
    object: int | tuple | str

    def __init__(self, subject: int, property: int, object: int | tuple | str):
        self.subject = subject
        self.property = property
        self.object = object

