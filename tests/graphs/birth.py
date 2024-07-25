from test_graph import TestGraph
from globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Single birth',
    input_text = 'Cajetan Tschudi was born on 26.10.1787 in Naples.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.C38_personAppellationInALanguage, properties.P11_isAppellationForLanguageOf, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.C38_personAppellationInALanguage, properties.P13_refersToName, classes.E41_appellation, 'Cajetan Tschudi\n(Appellation)'],
        [classes.E67_birth, properties.P98_broughtIntoLife, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
        [classes.E67_birth, properties.P8_tookPlaceOnOrWithin, classes.C13_geographicalPlace, 'Naples\n(Geographical Place)']
    ]
))