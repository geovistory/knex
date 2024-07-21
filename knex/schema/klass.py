import gmpykit as kit

class Klass:

    def __init__(self, pk: int, label: str, identifier: str):
        self.pk = pk
        self.label = label
        self.identifier = identifier

    def __str__(self):
        return f'Class({self.pk}, {self.label}, {self.identifier})'
    
    def create_obj_str(self): 
        return f'Klass({self.pk}, "{self.label}", "{self.identifier}")'
    
    def create_pk_str(self):
        return f'class_{self.identifier}_{kit.camel_case(self.label)} = {self.pk}'