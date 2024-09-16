from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Person',
    input_text = 'Julius Cesar.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.C38_personAppellationInALanguage, properties.P11_isAppellationForLanguageOf, classes.E21_person, 'Julius Cesar\n(Person)'],
        [classes.C38_personAppellationInALanguage, properties.P13_refersToName, classes.E41_appellation, 'Julius Cesar\n(Appellation)'],
    ]
))