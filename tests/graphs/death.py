import knex

def test_death_ping(eta):
    pass

def test_death_person_date(eta):

    texts = [
        'Cajetan Tschudi died in 1855.'
    ]

    for text in texts:
        knex.init(ask_llm=False)
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]

        try:
            assert line1['subject_class_pk'] == 63 # Death
            assert line1['property_pk'] == 88      # was death of
            assert line1['object_class_pk'] == 21  # Person
        except: raise Exception(f'[TEST] > ERROR in test_death_person_date, "was death of" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 63 # Death
            assert line2['property_pk'] == 72      # at some time within
            assert line2['object_class_pk'] == 335 # Person
        except: raise Exception(f'[TEST] > ERROR in test_death_person_date, "at some time within" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')


def test_death_person_place(eta):

    texts = [
        'Cajetan Tschudi died in Naples.'
    ]
    
    for text in texts:
        knex.init(ask_llm=False)
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]

        try:
            assert line1['subject_class_pk'] == 63 # Death
            assert line1['property_pk'] == 88      # was death of
            assert line1['object_class_pk'] == 21  # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_death_person_place, "was death of" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 63 # Death
            assert line2['property_pk'] == 1599    # took place at
            assert line2['object_class_pk'] == 363 # Geographical place
        except: 
            raise Exception(f'[TEST] > ERROR in test_death_person_place, "took place at" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')


def test_death_person_date_place(eta):

    texts = [
        'Cajetan Tschudi died in 1855, in Naples.'
    ]
    
    for text in texts:
        knex.init(ask_llm=False)    
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]
        line3 = response.graph_df.iloc[2]

        try:
            assert line1['subject_class_pk'] == 63 # Death
            assert line1['property_pk'] == 88      # was death of
            assert line1['object_class_pk'] == 21  # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_death_person_date_place, "was death of" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 63 # Death
            assert line2['property_pk'] == 72      # at some time within
            assert line2['object_class_pk'] == 335 # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_death_person_date_place, "at some time within" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')

        try:
            assert line3['subject_class_pk'] == 63 # Death
            assert line3['property_pk'] == 1599    # took place at
            assert line3['object_class_pk'] == 363 # Geographical place
        except:
            raise Exception(f'[TEST] > ERROR in test_death_person_date_place, "took place at" statement.\nFound: {line3['subject_class_pk']};{line3['property_pk']};{line3['object_class_pk']}')