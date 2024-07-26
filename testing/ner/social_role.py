from ..schema import TestNER
from ..globals import ner_tests


ner_tests.append(TestNER(
    name='Social Role, princess',
    input_text='Cajetan Tschudi was a princess of France.',
    entities=[{'text': 'a princess of France', 'type': 'SOCIAL_ROLE'}]
))

ner_tests.append(TestNER(
    name='Social Role, queen',
    input_text='Cajetan Tschudi was a queen of France.',
    entities=[{'text': 'a queen of France', 'type': 'SOCIAL_ROLE'}]
))

ner_tests.append(TestNER(
    name='Social Role, prince',
    input_text='Cajetan Tschudi was a prince of France.',
    entities=[{'text': 'a prince of France', 'type': 'SOCIAL_ROLE'}]
))

ner_tests.append(TestNER(
    name='Social Role, king',
    input_text='Cajetan Tschudi was a king of France.',
    entities=[{'text': 'a king of France', 'type': 'SOCIAL_ROLE'}]
))