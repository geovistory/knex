import knex

text = """
Cajetan Tschudi was born on 26.10.1787 in Naples
Cajetan Tschudi died in 1855
Cajetan Tschudi was Catholic
Cajetan Tschudi was from Glaris and Ennenda (now a commune of Glaris)
Pasqual is the father of Cajetan Tschudi
Cajetan Tschudi married Maria Carolina, princess of Liguoro, in 1822
Cajetan Tschudi was a prisoner of war in France from 1812 to 1813
In 1821, Cajetan Tschudi tried to create Swiss regiments in Naples
Cajetan Tschudi became major of the Guard in Naples in 1822
Cajetan Tschudi was field-marshal and governor of Naples in 1824
Cajetan Tschudi served as chargé d'affaires of the Two-Sicilian Kingdom in Bern from 1832 to 1834
Cajetan Tschudi was sent to Vienna and Constantinople
Cajetan Tschudi received the title of count napolitain in 1846.
"""

knex.run(text, visual=True, debug=True)
