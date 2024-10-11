import os, sys
from langchain_community.callbacks.manager import get_openai_callback
import knex
import geovpylib.database as db
import gmpykit as kit
from datetime import datetime

knex_nb = 100

eta = kit.Eta()
knex.init('openai', 'gpt-4o')
# knex.init('ollama', 'llama3.1', 'http://localhost:11434')
# knex.init('ollama', 'llama3.1', 'http://127.0.0.1:5000')
db.connect_yellow('switzerland_and_beyond')


table = db.query('select url, name, notice from hls.person')
texts = table.sample(knex_nb).copy()

texts['notice'] = texts['name'] + ':\n' + texts['notice']
texts.reset_index(inplace=True, drop=True)


begin_time = datetime.now()
with get_openai_callback() as cb:
    eta.begin(len(texts), 'Run KNEX')
    for _, text in texts.iterrows():

        # Prepare disk
        dir_name = 'knex_poc_hls_extract'
        file_name = kit.to_snake_case(text['name'])
        root_path = f'./{dir_name}/{file_name}/'
        if not os.path.exists(root_path): os.mkdir(root_path)
        with open(root_path + 'log.txt', 'w') as file:

            # initialize logs
            file.write(text['url'])
            file.write('\n\n' + kit.wrap(text['notice']))
            file.write('\n\n---------------\n\n')

            # Redirect logs to a file
            sys.stdout = file

            # Extract the information
            graph = knex.knowledge_extraction(text, verbose=True)

            # Save the result
            sys.stdout = open(os.devnull, 'w')
            graph.get_visuals(root_path + 'graph.html')
            sys.stdout = sys.__stdout__
            df = graph.to_dataframe()
            df.to_csv(root_path + 'graph.csv')
        eta.iter()
    eta.end()
    end_time = datetime.now()

    print()
    print(f'FOR {len(texts)} PERSONS:')
    print(f"Total Tokens: {kit.readable_number(cb.total_tokens)}")
    print(f"Prompt Tokens: {kit.readable_number(cb.prompt_tokens)}")
    print(f"Completion Tokens: {kit.readable_number(cb.completion_tokens)}")
    print(f"Total Cost (USD): ${cb.total_cost}")
    print(f"Total execution time: {end_time - begin_time}")
    print()
    print('AVERAGE FOR 1 PERSON')
    print(f"Total Tokens: {kit.readable_number(cb.total_tokens / len(texts))}")
    print(f"Prompt Tokens: {kit.readable_number(cb.prompt_tokens / len(texts))}")
    print(f"Completion Tokens: {kit.readable_number(cb.completion_tokens / len(texts))}")
    print(f"Total Cost (USD): ${cb.total_cost / len(texts)}")
    print(f"Total execution time: {(end_time - begin_time) / len(texts)}")
    print()
    print(f'ESTIMATION FOR ALL HLS PERSONS ({len(table)})')
    print(f"Total Tokens: {kit.readable_number((cb.total_tokens / len(texts)) * len(table))}")
    print(f"Prompt Tokens: {kit.readable_number((cb.prompt_tokens / len(texts)) * len(table))}")
    print(f"Completion Tokens: {kit.readable_number((cb.completion_tokens / len(texts)) * len(table))}")
    print(f"Total Cost (USD): ${(cb.total_cost / len(texts)) * len(table)}")
    print(f"Total execution time: {((end_time - begin_time) / len(texts)) * len(table)}")
    
kit.readable_number