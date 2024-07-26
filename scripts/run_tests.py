from testing import ner_tests, graph_tests


for test in ner_tests:
    test.exec()

for test in graph_tests:
    test.exec()