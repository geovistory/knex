from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Religion',
    input_text = 'Catholic.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.C11_appellationInALanguage, properties.P11_isAppellationForLanguageOf, classes.C23_religiousIdentity, 'Catholic\n(Religious Identity)'],
        [classes.C11_appellationInALanguage, properties.P13_refersToName, classes.E41_appellation, 'Catholic\n(Appellation)'],
    ]
))