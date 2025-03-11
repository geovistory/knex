import os, sys
from langchain_community.callbacks.manager import get_openai_callback
import knex
import geovpylib.database as db
import gmpykit as kit
from datetime import datetime
from geovpylib.ontology import classes as c, properties as p

eta = kit.Eta()
knex.init('openai', 'gpt-4o') # Commented out to avoid mistake run
# knex.init('ollama', 'llama3.1', 'http://localhost:11434') # Ollama
# knex.init('ollama', 'llama3.1', 'http://127.0.0.1:5000') # Ollama through proxy
db.connect_yellow('switzerland_and_beyond')

# Read HLS notices from Yellow and extract some of them
table = db.query('select url, name, notice from hls.person')

# Edit the notices
table['notice'] = table['name'] + ':\n' + table['notice']
table.reset_index(inplace=True, drop=True)

# Shuffle, so that we have a good estimation for the rest
table = table.sample(frac=1)

eta.begin(len(table), 'Extract KG from HLS')
for _, row in table.iterrows():
    try:

        # Prepare disk
        dir_name = '../hls-knowledge-graphs'
        file_name = kit.to_snake_case(row['name'])
        path = f'./{dir_name}/{file_name}.csv'

        # If already exist, go next
        if os.path.exists(path):
            continue
        
        # Extract the knowledge graph
        graph = knex.knowledge_extraction(row['notice'], verbose=False)

        # Add the URI
        if ', ' in row['name']:
            splitted = row['name'].split(', ')
            name = splitted[1] + ' ' + splitted[0]
        else:
            name = row['name']
        person = graph.create_entity(c.E21_person, name)
        uri = graph.create_entity(c.C30_uniformResourceIdentifierUri, row['url'])
        appellation = graph.create_entity(c.E41_appellation, row['url'])
        graph.create_triple(person, p.P28_sameAsUriOwlSameas, uri)
        graph.create_triple(uri, p.P21_hasValue, appellation)

        # Save the graph
        df = graph.to_dataframe()
        df.to_csv(path)
    
    except Exception as error:
        eta.print('>>>   THIS GUY FAILED: ' + str(row['name']) + " - " + str(row['url']) + '   <<<')
        continue

    eta.iter()
eta.end()
