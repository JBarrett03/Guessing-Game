from pydantic import BaseModel, ConfigDict

class CharacterRead(BaseModel):

    id: int
    name: str
    gender: str | None = None
    devil_fruit: str | None = None
    devil_fruit_type: str | None = None
    haki: str | None = None
    first_appearance_arc: str | None = None
    affiliation: str | None = None

    model_config = ConfigDict(from_attributes=True)