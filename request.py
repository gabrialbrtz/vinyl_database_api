from pydantic import BaseModel


class VinylRequest(BaseModel):
    """
    BaseModel Class Vinyl to represent the body of the petition
    """
    id: str = None
    name: str
    artist: str
    label: str
    release_year: str
