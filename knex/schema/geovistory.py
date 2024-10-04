import geovpylib.database as db
from .graph import Graph
from ..constants import classes as c

class GeovistoryDB:
    """
    This class is a GeovistoryDB wrapper that can do a lot of different things
    """


    def __init__(self, environment: str = 'prod', pk_project: int = -1, execute: bool = False):
        """
        Args:
            environment (str): on which environment should the object work on.
            pk_project (int): on which project should the object work in.
            execute (bool): safeguard to first test. If true, will make query directly in production. Only do when sure.
        """

        db.connect_geovistory(environment, pk_project, execute, skip_protection=True)


    def create_graph(graph: Graph):

        entities, triples, _, _ = graph.dataframes()

        # Filter out appellations (dedicated table)
        appellation_classes = [c.E41_appellation, c.E62_string, c.C2_chunk]
        appellations = entities[[fk_class in appellation_classes for fk_class in entities['fk_class']]].copy()
        appellations['pk_gv'] = db.appellations.create()

        # Filter out time primitives (dedicated table)
        time_primitives_classes = [c.E61_timePrimitive]
        time_primitives = entities[[fk_class in time_primitives_classes for fk_class in entities['fk_class']]]

        # Filter out dimensions (dedicated table)
        dimensions_classes = [c.C13_length, c.E54_dimension, c.C1_duration, c.C15_weight]
        dimensions = entities[[fk_class in dimensions_classes for fk_class in entities['fk_class']]]

        # Filter out lang_string (dedicated table)
        lang_strings_classes = [c.C14_uniformResourceLocatorUrl, c.C10_bibliographicCitation, c.C11_reference, c.C16_text, c.C15_shortTitle]
        lang_strings = entities[[fk_class in lang_strings_classes for fk_class in entities['fk_class']]]

        # Filter out languages (dedicated table)
        languages_classes = [c.E56_language]
        languages = entities[[fk_class in languages_classes for fk_class in entities['fk_class']]]

        # Filter out places (dedicated table)
        places_classes = [c.E53_place]
        places = entities[[fk_class in places_classes for fk_class in entities['fk_class']]]

        # Filter out text properties (dedicated table)
        text_properties_classes = [c.F1_work, c.F2_expression, c.F3_manifestationProductType, c.C20_comment]
        text_properties = entities[[fk_class in text_properties_classes for fk_class in entities['fk_class']]]

        entities['pk_gv'] = db.res
