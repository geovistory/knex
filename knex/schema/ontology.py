from typing import List
from .klass import Klass
from .property import Property


class Ontology:

    classes: List[Klass] = []
    properties: List[Property] = []

    def __init__(self): pass

    def set_classes(self, classes: List[Klass]):
        self.classes = classes
    
    def set_properties(self, properties: List[Property]):
        self.properties = properties

    def find_class(self, input: int | str):
        if isinstance(input, int): selection = [klass for klass in self.classes if input == klass.pk]
        elif isinstance(input, str): selection = [klass for klass in self.classes if input == klass.label]

        if len(selection) == 0: raise Exception(f'Unknown class "{input}"')
        elif len(selection) == 1: return selection[0]
        else: raise Exception(f'Multiple classes found with "{input}"')

    def find_property(self, input: int | str):
        if isinstance(input, int): selection = [property for property in self.properties if input == property.pk]
        elif isinstance(input, str): selection = [property for property in self.properties if input == property.label]

        if len(selection) == 0: raise Exception(f'Unknown property "{input}"')
        elif len(selection) == 1: return selection[0]
        else: raise Exception(f'Multiple properties found with "{input}"')

        