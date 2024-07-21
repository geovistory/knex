

class Profile:

    def __init__(self, pk: int, label: str):
        self.pk = pk
        self.label = label

    def __str__(self):
        return f'Profile({self.pk}, {self.label})'