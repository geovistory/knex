from typing import List, Dict
from knex import extraction, KnexOptions

class TestNER:

    def __init__(self,
                 name: str,
                 input_text: str,
                 entities: List[Dict]
                 ):
        self.name = name
        self.input_text = input_text
        self.should_entities = entities

    
    def exec(self):
      
        print(f'> Running NER tests "{self.name}"...', end=' ')

        options = KnexOptions(compute_assertions=False)
        response = extraction(self.input_text, options)

        doc_entities = []
        for doc in response.docs:
            for ent in doc.ents:
                doc_entities.append({'text': ent.text, 'type': ent.label_})    

        # Check if all needed entities are in the spacy document
        for should_entity in self.should_entities:
            found_and_correct = False
            for doc_entity in doc_entities:
                if doc_entity['text'] == should_entity['text'] and doc_entity['type'] == should_entity['type']:
                    found_and_correct = True
                    break
            if not found_and_correct: 
                self.report_entity_missing(should_entity, doc_entities)

        print('✅')


    def report_entity_missing(self, should: Dict, entities: List[Dict]):
        print(f'❌\n\n>>> NER test "{self.name}" failed')
        print(f'>>> Entity list should contain:\n     "{should['text']}": "{should['type']}"')
        print(f'>>> Entities list:')
        for ent_str in map(lambda ent: f'"{ent['text']}": "{ent['type']}"', entities):
            print('    ', ent_str)
        exit()