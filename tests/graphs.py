import knex
from ontology import *
from gmpykit import Eta
eta = Eta()


def test_birth_1(eta):
    text = 'Cajetan Tschudi was born on 26.10.1787 in Naples.'
    knex.init(ask_llm=False, visual=False)
    triples = knex.run(text).graph_df.to_dict(orient='records')
    needed = [
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P11_isAppellationForLanguageOf, 'object_class_pk': class_E21_person, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P13_refersToName, 'object_class_pk': class_E41_appellation, 'object_label': 'Cajetan Tschudi\n(Appellation)'},
        {'subject_class_pk': class_E67_birth, 'property_pk': property_P98_broughtIntoLife, 'object_class_pk': class_E21_person, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': class_E67_birth, 'property_pk': property_P82_atSomeTimeWithin, 'object_class_pk': class_E61_timePrimitive, 'object_label': '(1787, 10, 26)\n(Time Primitive)'},
        {'subject_class_pk': class_E67_birth, 'property_pk': property_P6_tookPlaceAt, 'object_class_pk': class_C13_geographicalPlace, 'object_label': 'Naples\n(Geographical Place)'},
    ]
    is_needed_in_triples(triples, needed, 'test_birth_1')


def test_death_1(eta):
    text = 'Cajetan Tschudi died in 1855.'
    knex.init(ask_llm=False, visual=False)
    triples = knex.run(text).graph_df.to_dict(orient='records')
    needed = [
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P11_isAppellationForLanguageOf, 'object_class_pk': class_E21_person, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P13_refersToName, 'object_class_pk': class_E41_appellation, 'object_label': 'Cajetan Tschudi\n(Appellation)'},
        {'subject_class_pk': class_E69_death, 'property_pk': property_P100_wasDeathOf, 'object_class_pk': class_E21_person, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': class_E69_death, 'property_pk': property_P82_atSomeTimeWithin, 'object_class_pk': class_E61_timePrimitive, 'object_label': '(1855, <Na>, <Na>)\n(Time Primitive)'},
    ]
    is_needed_in_triples(triples, needed, 'test_death_1')


def test_confession_1(eta):
    text = 'Cajetan Tschudi was Catholic.'
    knex.init(ask_llm=False, visual=False)
    triples = knex.run(text).graph_df.to_dict(orient='records')
    needed = [
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P11_isAppellationForLanguageOf, 'object_class_pk': class_E21_person, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': class_C38_personAppellationInALanguage, 'property_pk': property_P13_refersToName, 'object_class_pk': class_E41_appellation, 'object_label': 'Cajetan Tschudi\n(Appellation)'},
        {'subject_class_pk': class_C11_appellationInALanguage, 'property_pk': property_P11_isAppellationForLanguageOf, 'object_class_pk': class_C23_religiousIdentity, 'object_label': 'Catholic\n(Religious Identity)'},
        {'subject_class_pk': class_C11_appellationInALanguage, 'property_pk': property_P13_refersToName, 'object_class_pk': class_E41_appellation, 'object_label': 'Catholic\n(Appellation)'},
        {'subject_class_pk': class_C23_religiousIdentity, 'property_pk': property_P36_pertainsTo, 'object_class_pk': class_E21_person},
    ]
    is_needed_in_triples(triples, needed, 'test_death_1')





##############################################################################################################################
############################################ Write tests above this line #####################################################
##############################################################################################################################

def is_needed_in_triples(triples, needed, function_name):
    for need in needed:
        found = False
        for triple in triples:
            valid = True
            for attr in need:
                if need[attr] != triple[attr]: 
                    valid = False
                    break
            if valid: 
                found = True

        if not found:
            raise Exception(f'\n[TEST] > Error when running "{function_name}", missing triple "{need}".')


functions = list(map(lambda fct_name: globals()[fct_name], filter(lambda name: name.startswith('test_'), dir())))

eta.begin(len(functions), 'Runing test functions')
for fct in functions:
    fct(eta)
    eta.iter()
eta.end()

print(f'[TEST] > {len(functions)} tests passed.' )
