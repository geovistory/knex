from ..schema import TestNER
from ..globals import ner_tests


ner_tests.append(TestNER(
    name='Religion, protestant',
    input_text='Cajetan Tschudi was protestant.',
    entities=[{'text': 'protestant', 'type': 'RELIGION'}]
))

ner_tests.append(TestNER(
    name='Religion, catholic',
    input_text='Cajetan Tschudi was catholic.',
    entities=[{'text': 'catholic', 'type': 'RELIGION'}]
))

ner_tests.append(TestNER(
    name='Religion, chrétien',
    input_text='Cajetan Tschudi was chrétien.',
    entities=[{'text': 'chrétien', 'type': 'RELIGION'}]
))