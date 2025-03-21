from unidecode import unidecode

occupations_white_list = list(map(lambda text: unidecode(text),
[
'Executive Committee Member',
'Landamman',
'Merchant',
'Assistant',
'Printer',
'Agriculturalist', 'Agriculturer',
'Commissioner',
'Cadet',
'Prefect',
'Attaché Honoraire',
'Member',
'Candle Maker',
'Servant',
'District Judge',
'Vigneron',
'Mandat',
'Police Director',
'Television producer',
'Correspondent',
'Editor-in-Chief',
'Officeholder',
'Lieutenant General',
'Chief of Staff',
'Textile worker',
'Patriote',
'Administrator',
'Doctor',
'Conservator',
'General',
'Butcher Master', 'Master Blacksmith', 'master tailor of crystals'
'Advocate',
'Restaurateur',
'Lieutenant-Colonel',
'Mercenary',
'Councilor',
'Draftsman',
'Professor of Cuisine',
'Farmer',
'Abbé',
'Corps Commander',
'Chocolate Manufacturer',
'Medical Assistant',
'Conductor',
'Pastor',
'Rentier',
'Teacher',
'Violinist',
'Under-Secretary of State',
'Director of Public Customs and exchange',
'Maître de gymnase',
'Justice',
'Member of the Petit Conseil',
'Journalist',
'Musician',
'Agricultural Statistician',
'Judge',
'Suppléant',
'Officer',
'Curé',
'Archidiacre',
'Jurist',
'Collaborator',
'Director General',
'Auditor',
'Syndic',
'President',
'Chief Conductor',
'Bailiff',
'Agricultur',
'Captain',
'Warrior',
'Treasurer',
'Prevot',
'War Commissioner',
'Bourgeois',
'Agriculturist',
'Banker',
'Lawmaker',
'Member of the délégation de la ville',
'Editor',
'Member of the Conseil aux Etats',
'Archivist',
'Member of the Deux-Cents',
'Banneret',
'Freuler',
'Instituteur',
'Weaver',
'Directeur des sels',
'Preacher',
'Administrateur',
'Commander',
'Comedian',
'Canton official',
'Legislator',
'Member of the General Council',
'Peasant',
'Writer',
'Engineer',
'Assistant Inspector of Labor',
'State Councillor',
'Captain-Lieutenant',
'Architect',
'Lieutenant',
'Politician',
'Notary Apostolic',
'Canon',
'Bailli',
'Film Director',
'Pianist',
'Commissaire des Sels',
'Veterinarian',
'Flight Attendant',
'Ensign',
'Member of the Conseil des Deux-Cents',
'Music Teacher',
'Actuary',
'Professor',
'Sous-Prefet',
'Notary',
'Innkeeper',
'Stage Manager',
'Avoyer',
'Member of the Grand Council',
'Soldier',
'Lieutenant-General',
'Amman',
'Painter',
'Commandant',
'Horticulturist',
'Podestat',
'Inspector',
'General-Major',
'Councillor',
'Custodian', 'Custode',
'Council Member',
'Employee',
'Principal Stage Director',
'Chief Editor',
'Avocat',
'Greffier',
'Imprinter',
'Conseil d\'Etat Member',
'Cavalier',
'Colonel',
'Lawyer',
'Secretary', "Secretaire de la Societe grisonne d'agriculture",
'Volunteer',
'Stage Director',
'Landowner',
'Burgomaster',
'Actor',
'Central Secretary',
'Milk Producer',
'Catechist',
'Organist',
'Landscape Painter',
'Enseigne',
'Trésorier',
'Pharmacist',
'Physician',
'Abbot',
'Brigadier',
'Bishop',
'Commander-in-Chief',
'Chancellor',
'Delegate',
'Cult Leader',
'Vice-president of a court',
'Carpenter',
'Director of public customs and exchange',
'Vice-président du tribunal cantonal',
'Guardian of Convents'
]))