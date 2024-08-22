from unidecode import unidecode

social_role_white_list = list(map(lambda text: unidecode(text),
[
    'Judge of Instruction',
    'Chancellor of State',
    'Princess',
    'Queen',
    'Prince',
    'King',
    'Conseiller d\'Etat',
    'Conseiller national',
    'Conseiller fédéral',
    'Deputy',
    'City Secretary',
    'Procureur Général',
    'Member of the Grand Conseil',
    'Cantonal Judge',
]))