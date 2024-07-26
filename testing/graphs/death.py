from ..schema import TestGraph
from ..globals import graph_tests
from knex import classes, properties

graph_tests.append(TestGraph(
    name = 'Single death with date',
    input_text = 'Cajetan Tschudi died in 1855.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E69_death, properties.P100_wasDeathOf, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E69_death, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1855, <Na>, <Na>)\n(Time Primitive)'],
    ]
))

graph_tests.append(TestGraph(
    name = 'Single death with place',
    input_text = 'Cajetan Tschudi died in Naples.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E69_death, properties.P100_wasDeathOf, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E69_death, properties.P8_tookPlaceOnOrWithin, classes.C13_geographicalPlace, 'Naples\n(Geographical Place)']
    ]
))

graph_tests.append(TestGraph(
    name = 'Single death with date and place',
    input_text = 'Cajetan Tschudi died on 26.10.1787 in Naples.',
    compute_assertions = False,
    should_columns = ['subject_class_pk', 'property_pk', 'object_class_pk', 'object_label'],
    should_data = [
        [classes.E69_death, properties.P100_wasDeathOf, classes.E21_person, 'Cajetan Tschudi\n(Person)'],
        [classes.E69_death, properties.P82_atSomeTimeWithin, classes.E61_timePrimitive, '(1787, 10, 26)\n(Time Primitive)'],
        [classes.E69_death, properties.P8_tookPlaceOnOrWithin, classes.C13_geographicalPlace, 'Naples\n(Geographical Place)']
    ]
))