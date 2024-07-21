from typing import List
import requests
import gmpykit as kit
from knex import Profile, Klass, Property

eta = kit.Eta()


def fetch_profiles():
    print('> Fetching profiles...', end=' ')

    url = 'https://ontome.net/api/profiles.json?lang=en'
    response = requests.get(url).json()

    profiles = []
    for element in response:
        profiles.append(Profile(element['profileID'], element['profileLabel']))

    print('Done')

    return profiles


def fetch_classes(profiles: List[Profile]):
    eta.begin(len(profiles), '> Fetching classes')

    classes = []
    have_classes = set()
    for profile in profiles:
        url = f'https://ontome.net/api/classes-profile.json?lang=en&available-in-profile={profile.pk}'
        response = requests.get(url).json()

        for element in response:
            if element['classID'] not in have_classes:
                classes.append(Klass(element['classID'], element['classLabel'], element['classIdentifierInNamespace']))
                have_classes.add(element['classID'])

        eta.iter()
    eta.end()

    return classes


def fetch_properties(profiles: List[Profile]):
    eta.begin(len(profiles), '> Fetching properties')

    properties = []
    have_properties = set()
    for profile in profiles:
        url = f'https://ontome.net/api/properties-profile.json?lang=en&available-in-profile={profile.pk}'
        response = requests.get(url).json()

        for element in response:
            if element['propertyID'] not in have_properties:
                properties.append(Property(element['propertyID'], element['propertyLabel'], element['propertyIdentifierInNamespace']))
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
content = ""

# Add all the classes
for klass in classes:
    content += klass.create_pk_str().replace('-', '_') + '\n'

content += '\n'

# Add all the properties
for property in properties:
    content += property.create_pk_str().replace('-', '_') + '\n'

# Write on disk
file = open(path, "w")
file.write(content)
file.close()