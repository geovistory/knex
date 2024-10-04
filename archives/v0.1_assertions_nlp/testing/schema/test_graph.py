from typing import List
from knex import extraction, KnexOptions

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
        
        options = KnexOptions(compute_assertions=self.compute_assertions)
        response = extraction(self.input_text, options)
        values = response.graph[self.should_columns].values.tolist()

        # Check if the graph has everything needed
        for data in self.should_data:
            if not data in values: 
                self.report_graph_missing(data, response.graph[self.should_columns])

        print('✅')


    def report_graph_missing(self, should: List[str | int], graph):
        print(f'❌\n\n>>> Graph test "{self.name}" failed')
        print(f'>>> Graph should have had: {should}')
        print('>>> But the graph is:')
        print(graph)
        exit()

    

        