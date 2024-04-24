import knex

text = """
Cajetan Tschudi was born on 26.10.1787 in Naples.
Cajetan Tschudi died in 1855.
Cajetan Tschudi was Catholic.
Cajetan Tschudi was from Glaris and Ennenda (now a commune of Glaris).
Pasqual is the father of Cajetan Tschudi.
Cajetan Tschudi married Maria Carolina, princess of Liguoro, in 1822.
Cajetan Tschudi was a prisoner of war in France from 1812 to 1813.
In 1821, Cajetan Tschudi tried to create Swiss regiments in Naples.
Cajetan Tschudi became major of the Guard in Naples in 1822.
Cajetan Tschudi was field-marshal and governor of Naples in 1824.
Cajetan Tschudi served as chargé d'affaires of the Two-Sicilian Kingdom in Bern from 1832 to 1834.
Cajetan Tschudi was sent to Vienna and Constantinople.
Cajetan Tschudi received the title of count napolitain in 1846.
"""


# text = "Tschudi, Cajetan. Naît le 26.10.1787 à Naples, meurt 1855, catholique, de Glaris et Ennenda (aujourd'hui commune de Glaris). Fils de Pasqual (https://hls-dhs-dss.ch/fr/articles/024356/2012-11-21/). Marié(e) (1822) à Maria Carolina, princesse de Liguoro, sans doute de la famille des marquis de Presicce. Prisonnier de guerre en France en 1812-1813. Dès 1821, Cajetan Tschudi s'efforça de recréer des régiments suisses à Naples, où il devint major de la Garde (1822), feld-maréchal et gouverneur de la ville de Naples (1824). Chargé d'affaires du royaume des Deux-Siciles à Berne (1832-1834), puis envoyé à Vienne et Constantinople, Cajetan Tschudi aurait reçu le titre de comte napolitain en 1846."

knex.init(ask_llm=False, visual=True, debug=True)
knex.run(text.strip())
