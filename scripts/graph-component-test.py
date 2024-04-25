import sys
import knex

text = sys.argv[1]
debug_list = sys.argv[2].split(',')

knex.init(ask_llm=False, visual=True, debug_list=debug_list)
response = knex.run(text)

print('>>>> FEEDBACK <<<<')
print(response.feedback)
