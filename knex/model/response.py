import pandas as pd

class Response:

    def __init__(self, input_text: str, assertions: str, graph_df: pd.DataFrame):
        self.input_text = input_text
        self.assertions = assertions
        self.graph_df = graph_df
