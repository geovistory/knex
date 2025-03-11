import os
import pandas as pd
import knex

sparql_url = ""
graph_uri = "http://information-ocean.geovistory.org/hls"
base_uri = ""


folder = "../hls-knowledge-graphs/"
for file in os.listdir(folder):
    df = pd.read_csv(folder + file)
    graph = knex.Graph.from_dataframe(df)
    graph.to_sparql(sparql_url, graph_uri, )
    print(df)
    break
