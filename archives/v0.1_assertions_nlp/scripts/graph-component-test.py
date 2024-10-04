import sys
from knex import extraction

text = sys.argv[1]
debug_list = sys.argv[2].split(',') if len(sys.argv) >= 3 else []

response = extraction(text, debug_list=debug_list, compute_assertions=False, return_feedbacks=True)

print('\n>>>> FEEDBACK <<<<')
print(response.feedback)


print('\n>>> GRAPH <<<')
print(response.graph[['subject_label', 'property_label', 'object_label']])