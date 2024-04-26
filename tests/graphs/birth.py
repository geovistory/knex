import knex

def test_birth_ping(eta):
    pass

def test_birth_person_date(eta):

    texts = [
        'Gaétan Muck is born on 01.09.1992.',
        'Gaétan Muck is born in 1992.'
    ]

    for text in texts:
        knex.init(ask_llm=False)
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]

        try:
            assert line1['subject_class_pk'] == 61 # Birth
            assert line1['property_pk'] == 86      # brought into life
            assert line1['object_class_pk'] == 21  # Person
        except: raise Exception(f'[TEST] > ERROR in test_birth_person_date, "brought into life" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 61 # Birth
            assert line2['property_pk'] == 72      # at some time within
            assert line2['object_class_pk'] == 335  # Person
        except: raise Exception(f'[TEST] > ERROR in test_birth_person_date, "at some time within" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')


def test_birth_person_place(eta):

    texts = [
        'Gaétan Muck is born in Mulhouse.'
    ]

    for text in texts:
        knex.init(ask_llm=False)
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]

        try:
            assert line1['subject_class_pk'] == 61 # Birth
            assert line1['property_pk'] == 86      # brought into life
            assert line1['object_class_pk'] == 21  # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_birth_person_place, "brought into life" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 61 # Birth
            assert line2['property_pk'] == 1599    # took place at
            assert line2['object_class_pk'] == 363 # Geographical place
        except: 
            raise Exception(f'[TEST] > ERROR in test_birth_person_place, "took place at" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')


def test_birth_person_date_place(eta):
    
    texts = [
        'Gaétan Muck is born on 01.09.1992, in Mulhouse.',
        'Cajetan Tschudi was born on 26.10.1787 in Naples.'
    ]

    for text in texts:
        knex.init(ask_llm=False)
        response = knex.run(text)

        line1 = response.graph_df.iloc[0]
        line2 = response.graph_df.iloc[1]
        line3 = response.graph_df.iloc[2]

        try:
            assert line1['subject_class_pk'] == 61 # Birth
            assert line1['property_pk'] == 86      # brought into life
            assert line1['object_class_pk'] == 21  # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_birth_person_date_place, "brought into life" statement.\nFound: {line1['subject_class_pk']};{line1['property_pk']};{line1['object_class_pk']}')

        try:
            assert line2['subject_class_pk'] == 61 # Birth
            assert line2['property_pk'] == 72      # at some time within
            assert line2['object_class_pk'] == 335  # Person
        except: 
            raise Exception(f'[TEST] > ERROR in test_birth_person_date_place, "at some time within" statement.\nFound: {line2['subject_class_pk']};{line2['property_pk']};{line2['object_class_pk']}')

        try:
            assert line3['subject_class_pk'] == 61 # Birth
            assert line3['property_pk'] == 1599    # took place at
            assert line3['object_class_pk'] == 363 # Geographical place
        except: 
            raise Exception(f'[TEST] > ERROR in test_birth_person_date_place, "took place at" statement.\nFound: {line3['subject_class_pk']};{line3['property_pk']};{line3['object_class_pk']}')