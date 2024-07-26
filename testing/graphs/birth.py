from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Single birth with date',
    input_text = 'Cajetan Tschudi was born on 26.10.1787.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P98_broughtIntoLife, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
    ]
))

graph_tests.append(TestGraph(
    name = 'Single birth with place',
    input_text = 'Cajetan Tschudi was born in Naples.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P98_broughtIntoLife, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E67_birth, properties.P8_tookPlaceOnOrWithin, classes.C13_geographicalPlace, 'Naples\n(Geographical Place)']
    ]
))

graph_tests.append(TestGraph(
    name = 'Single birth with date and place',
    input_text = 'Cajetan Tschudi was born on 26.10.1787 in Naples.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P98_broughtIntoLife, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
        [classes.E67_birth, properties.P8_tookPlaceOnOrWithin, classes.C13_geographicalPlace, 'Naples\n(Geographical Place)']
    ]
))