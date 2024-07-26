from ..schema import TestNER
from ..globals import ner_tests


ner_tests.append(TestNER(
    name='Date with "on" and numbers',
    input_text='Cajetan Tschudi was born on 26.10.1787.',
    entities=[{'text': 'on 26.10.1787', 'type': 'DATE'}]
))

ner_tests.append(TestNER(
    name='Date with "in" and numbers',
    input_text='Cajetan Tschudi was born in 26.10.1787.',
    entities=[{'text': 'in 26.10.1787', 'type': 'DATE'}]
))

ner_tests.append(TestNER(
    name='Date with explicit text',
    input_text='He was born the 1st January 2020.',
    entities=[{'text': 'the 1st January 2020', 'type': 'DATE'}]
))