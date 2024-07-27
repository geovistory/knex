from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties


graph_tests.append(TestGraph(
    name = 'Confession of a person',
    input_text = 'Alfred was protestant.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.C23_religiousIdentity, properties.P36_pertainsTo, classes.E21_person, 'Alfred\n(Person)'],
        [classes.C11_appellationInALanguage, properties.P11_isAppellationForLanguageOf, classes.C23_religiousIdentity, 'Protestant\n(Religious Identity)'],
        [classes.C11_appellationInALanguage, properties.P13_refersToName, classes.E41_appellation, 'Protestant\n(Appellation)'],
    ]
))
