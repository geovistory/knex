from typing import List
import pandas as pd
import knex

class TestGraph: 

    def __init__(self, 
                 name: str, 
                 input_text: str, 
                 should_columns: List[str], 
                 should_data: List[str | int],
                 compute_assertions: bool = True, 
                ):
        self.name = name
        self.input_text = input_text
        self.compute_assertions = compute_assertions
        self.should_columns = should_columns
        self.should_data = should_data


    def exec(self):

        print(f'> Running graph tests "{self.name}"...', end=' ')

        graph, feedback = knex.extract(self.input_text, compute_assertions=self.compute_assertions)
        values = graph[self.should_columns].values.tolist()

        # Check if the graph has everything needed
        for data in self.should_data:
            if not data in values: 
                self.report_graph_missing(data, graph[self.should_columns])

            
        # Check if the graph has not too much data
        for value in values:
            if not value in self.should_data:
                self.report_graph_has_too_much(value, graph[self.should_columns])

        print('✅')


    def report_graph_missing(self, should: List[str | int], graph):
        print(f'❌\n>>> Test "{self.name}" failed')
        print(f'>>> Graph should have had: {should}')
        print('>>> But the graph is:')
        print(graph)
        exit()
    

    def report_graph_has_too_much(self, value: List[str | int], graph):
        print(f'❌\n>>> Test "{self.name}" failed')
        print(f'    The graph has too much: {value}')
        print(graph)
        exit()


    

        