import knex
from gmpykit import Eta
eta = Eta()


def test_1(eta):
    text = 'Cajetan Tschudi was born on 26.10.1787 in Naples.'
    knex.init(ask_llm=False, visual=False)
    triples = knex.run(text).graph_df.to_dict(orient='records')
    needed = [
        {'subject_class_pk': 868, 'property_pk': 1111, 'object_class_pk': 21, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': 868, 'property_pk': 1113, 'object_class_pk': 40, 'object_label': 'Cajetan Tschudi\n(Appellation)'},
        {'subject_class_pk': 61, 'property_pk': 86, 'object_class_pk': 21, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': 61, 'property_pk': 72, 'object_class_pk': 335, 'object_label': '(1787, 10, 26)\n(Time Primitive)'},
        {'subject_class_pk': 61, 'property_pk': 1599, 'object_class_pk': 363, 'object_label': 'Naples\n(Geographical Place)'},
    ]
    is_needed_in_triples(triples, needed, 'test_1')

def test_2(eta):
    text = 'Cajetan Tschudi died in 1855.'
    knex.init(ask_llm=False, visual=False)
    triples = knex.run(text).graph_df.to_dict(orient='records')
    needed = [
        {'subject_class_pk': 868, 'property_pk': 1111, 'object_class_pk': 21, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': 868, 'property_pk': 1113, 'object_class_pk': 40, 'object_label': 'Cajetan Tschudi\n(Appellation)'},
        {'subject_class_pk': 63, 'property_pk': 88, 'object_class_pk': 21, 'object_label': 'Cajetan Tschudi\n(Person)'},
        {'subject_class_pk': 63, 'property_pk': 72, 'object_class_pk': 335, 'object_label': '(1855, <Na>, <Na>)\n(Time Primitive)'},
    ]
    is_needed_in_triples(triples, needed, 'test_2')

    




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
