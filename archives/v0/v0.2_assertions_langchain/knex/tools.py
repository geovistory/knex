from typing import Type
from .globals import schemas
from .model import ExtractedSchema

# Get the right schema class for the given topic. 
# If it does not exist, prints it out and return nothing
def get_schema(topic: str) -> Type:

    selection = list(filter(lambda schema: schema.topic == topic, schemas))

    if len(selection) == 0: print(f"[KNEX-INFO]: Missing Topic Schema <{topic}>.")
    else: return selection[0]