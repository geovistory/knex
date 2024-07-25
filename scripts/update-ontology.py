from typing import List, Dict
import requests
import gmpykit as kit

eta = kit.Eta()


def fetch_profiles() ->  List[Dict]:
    print('> Fetching profiles...', end=' ')

    url = 'https://ontome.net/api/profiles.json?lang=en'
    response = requests.get(url).json()

    profiles = []
    for element in response:
        profiles.append({'pk': element['profileID'], 'label': element['profileLabel']})

    print('Done')

    return profiles


def fetch_classes(profiles: List[Dict]) -> List[Dict]:
    eta.begin(len(profiles), '> Fetching classes')

    classes = []
    have_classes = set()
    for profile in profiles:
        url = f'https://ontome.net/api/classes-profile.json?lang=en&available-in-profile={profile["pk"]}'
        response = requests.get(url).json()

        for element in response:
            if element['classID'] not in have_classes:
                classes.append({'pk': element['classID'], 'label': element['classLabel'], 'id': element['classIdentifierInNamespace']})
                have_classes.add(element['classID'])

        eta.iter()
    eta.end()

    return classes


def fetch_properties(profiles: List[Dict]) -> List[Dict]:
    eta.begin(len(profiles), '> Fetching properties')

    properties = []
    have_properties = set()
    for profile in profiles:
        url = f'https://ontome.net/api/properties-profile.json?lang=en&available-in-profile={profile["pk"]}'
        response = requests.get(url).json()

        for element in response:
            if element['propertyID'] not in have_properties:
                properties.append({'pk': element['propertyID'], 'label': element['propertyLabel'], 'id': element['propertyIdentifierInNamespace']})
                have_properties.add(element['propertyID'])

        eta.iter()
    eta.end()

    return properties


# Fetch everything from OntoMe
profiles = fetch_profiles()
classes = fetch_classes(profiles)
properties = fetch_properties(profiles)

# Prepare writing on disk, a python file
path = 'knex/constants/ontology.py'
content = """from typing import List

class OntoObject:
    def __init__(self, pk: int, label: str, id: str):
        self.pk = pk
        self.label = label
        self.id = id

class Ontology:
    classes: List[OntoObject] = []
    properties: List[OntoObject] = []

    def __init__(self): 
        pass

    def klass(self, input: int | str) -> OntoObject:
        return self.__find(self.classes, input, 'class')

    def property(self, input: int | str) -> OntoObject:
        return self.__find(self.properties, input, 'property')

    def __find(self, ontoobjects: List[OntoObject], input: int | str, name=str) -> OntoObject:
        if isinstance(input, int): selection = [obj for obj in ontoobjects if input == obj.pk]
        elif isinstance(input, str): selection = [obj for obj in ontoobjects if input.lower() == obj.label.lower() or input.lower() == obj.id.lower()]

        if len(selection) == 0: raise Exception(f'Unknown ' + name + ' "' + input + '"')
        elif len(selection) == 1: return selection[0]
        else: raise Exception('Multiple ' + name + ' found with "' + input + '"')

ontology = Ontology()
"""

# Add all the classes
for property in classes:
    content += f"ontology.classes.append(OntoObject({property['pk']}, \"{property['label']}\", \"{property['id']}\"))\n"
content += '\n'
content += 'class PkClass:\n'
for klass in classes:
    content += f"   {klass['id']}_{kit.camel_case(klass['label'])} = {klass['pk']}\n".replace('-', '_')
content += '\classes = PkClass()\n\n'

# Add all the properties
for property in properties:
    content += f"ontology.properties.append(OntoObject({property['pk']}, \"{property['label']}\", \"{property['id']}\"))\n"
content += '\n'
content += 'class PkProperty:\n'
for property in properties:
    content += f"   {property['id']}_{kit.camel_case(property['label'])} = {property['pk']}\n".replace('-', '_')
content += '\nproperties = PkProperty()\n\n'

# Write on disk
file = open(path, "w")
file.write(content)
file.close()