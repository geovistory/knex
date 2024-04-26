from graphs import *
from gmpykit import Eta

eta = Eta()

functions = list(map(lambda fct_name: globals()[fct_name], filter(lambda name: name.startswith('test_'), dir())))

eta.begin(len(functions), 'Runing test functions')
for fct in functions:
    fct(eta)
    eta.iter()
eta.end()

print(f'[TEST] > {len(functions)} tests passed.' )


