import knex

text = """
René Dubois naît le 17.8.1905 aux Verrières, et meurt le 16.11.1976 à Marin-Epagnier, protestant, de Buttes.
Fils d'Henri Adolphe, fonctionnaire postal.
Marié(e) à Suzanne Mina Arnoux, Française, fille de Jules Cyprien.
Licence en sciences économiques à Neuchâtel.
Officier instructeur dès 1929.
Chef d'état-major des troupes d'aviation et de DCA (1953-1955).
Commandant de la brigade légère 1, de la division 2 (1958-1961), du corps d'armée de campagne 1 (1962-1967).
""".strip()

# text = """
# Armin Kellersberger naît le 18.12.1838 à Baden, meurt le 28.7.1905 à Baden, catholique, de Baden. 
# Fils de Josef, avocat, député au Grand Conseil et vice-président de la ville de Baden, et de Julia Brentano, de Laufenburg. 
# Marié(e) à 1) 1864 Blanka Dorer, fille d'Ignaz Eduard Dorer (https://hls-dhs-dss.ch/fr/articles/005488/2004-04-08/) (divorce en 1871), 2) 1877 Anna Maria Stolz, de Laufenburg, fille de Johann Baptist, hôtelier et conseiller. 
# Ecole cantonale d'Aarau, études de droit à Heidelberg, Munich et Zurich, brevet argovien d'avocat (1864). 
# Après avoir travaillé dans le bureau de son père, Armin Kellersberger ouvrit son étude à Laufenburg (1868-1877). 
# Membre du Conseil de ville (1872-1874), en outre vice-préfet du district de Laufenburg, puis greffier de Baden (1877-1880). 
# Président de la ville de Baden (1881-1893), Armin Kellersberger préserva la commune d'une ruine imminente, après la faillite du chemin de fer National-Suisse, en sollicitant un emprunt auprès de la Confédération et en contraignant la commune bourgeoise à un soutien financier.
# Député au Grand Conseil argovien (1875-1905, président en 1880-1881 et 1891-1892). Conseiller aux Etats (1881-1905, président en 1890-1891). 
# Major et commandant de bataillon, il se distingua sur des questions militaires, notamment les fortifications du Gothard et comme partisan de l'armement des troupes du landsturm (ce qui lui valut le surnom de "père du landsturm"). 
# Armin Kellersberger appartint d'abord à l'aile libérale, puis démocrate des radicaux. 
# Vice-président du parti radical argovien, il exerça un rôle modérateur et chercha en 1895 avec Arnold Künzli à susciter une fusion entre démocrates et libéraux. 
# Membre de la Constituante argovienne, il s'efforça en 1884-1885 de calmer les antagonismes confessionnels aggravés par le Kulturkampf. 
# Conseiller juridique de Brown Boveri et de la SA Motor (administrateur de 1896 à 1902), administrateur de la centrale électrique de Hagneck (président dès 1898), de la Société d'électricité de Baden (1903-1905) et des chemins de fer du Nord-Est (1894-1902). 
# Armin Kellersberger et son beau-fils Alfred Meyer entreprirent des fouilles sur leur propriété de Baden (1894-1898), qui mirent au jour des vestiges romains remarquables. 
# Grâce à son esprit de conciliation et à son large champ d'activités, tant juridiques que politiques, Armin Kellersberger fut l'un des politiciens argoviens les plus estimés de son temps.
# """.strip()


graph = 



extract = knex.extraction(text, verify=False, verbose=True)
tables = knex.extraction_to_tables(extract)

tables.to_csv('./persons.csv')



# knex.knowledge_extraction(text, verify=False, verbose=True, output_csv="graph.csv", output_html="graph.html")



# results = knex.extraction(text, verbose=True, verify=False)
# graph = knex.knowledge(results)
# graph.to_dataframe().to_csv('graph.csv', index=False)
# graph.get_visuals('./temp.html')