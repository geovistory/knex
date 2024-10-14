import knex
from knex.constants import classes as c, properties as p

graph = knex.Graph()

gaetan = graph.create_entity_aial(c.E21_person, 'Gaétan Muck')
birth = graph.create_entity(c.E67_birth, 'Gaétan Muck')
time_prim = graph.create_entity(c.E61_timePrimitive, '1992.09.01')

graph.create_triple(birth, p.P98_broughtIntoLife, gaetan)
graph.create_triple(birth, p.P82_atSomeTimeWithin, time_prim)


sub_graph = graph.get_subgraph(1, 20)
print(sub_graph.to_dataframe())