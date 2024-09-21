from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Date: default (at some time within)',
    input_text = 'Cajetan Tschudi was born the 26.10.1787.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
    ]
))

graph_tests.append(TestGraph(
    name = 'Date: at some time within (on)',
    input_text = 'Cajetan Tschudi was born on 26.10.1787.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
    ]
))

graph_tests.append(TestGraph(
    name = 'Date: at some time within (in)',
    input_text = 'Cajetan Tschudi was born in 26.10.1787.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E67_birth, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
    ]
))