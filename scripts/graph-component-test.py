import sys
from knex import extract, KnexOptions

text = sys.argv[1]
debug_list = sys.argv[2].split(',') if len(sys.argv) >= 3 else []

options = KnexOptions(compute_assertions=False, return_feedbacks=True)

response = extract(text, options, debug_list=debug_list)

print('\n>>>> FEEDBACK <<<<')
print(response.feedback)


print('\n>>> GRAPH <<<')
print(response.graph[['subject_label', 'property_label', 'object_label']])