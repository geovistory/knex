from testing import ner_tests, graph_tests
from datetime import datetime
import gmpykit as kit

test_nb = len(ner_tests) + len(graph_tests)
print(f'Run of {test_nb} begins...')

begin = datetime.now().timestamp()

for test in ner_tests:
    test.exec()

for test in graph_tests:
    test.exec()

end = datetime.now().timestamp()

print(f'Ran {test_nb} successful tests in {kit.readable_time(end - begin)}.')