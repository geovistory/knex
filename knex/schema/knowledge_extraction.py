import pandas as pd

class KnowledgeExtraction:

    def __init__(self, input_text: str, assertions: str, graph_df: pd.DataFrame, feedback: str):
        self.input_text = input_text
        self.assertions = assertions
        self.graph_df = graph_df
        self.feedback = feedback