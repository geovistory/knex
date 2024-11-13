from pydantic import BaseModel

class Assertion(BaseModel):
    topic: str = ''
    text: str = ''

    def __init__(self, topic, text):
        super().__init__()
        self.topic = topic
        self.text = text