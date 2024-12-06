from pydantic import BaseModel

class ExampleModel(BaseModel):
    id: int
    name: str
    description: str | None = None
