
class Triple:

    def __init__(self, subject: int, property: int, object: int):
        self.subject_pk = subject
        self.property_pk = property
        self.object_pk = object

    def __str__(self):
        return f'Triple({self.subject_pk}, {self.property_pk}, {self.object_pk})'