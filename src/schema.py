from pydantic import BaseModel

class PokemonSchame(BaseModel): # Schema de Dados.
    name:str
    type: str

    class Config:
        from_attributes = True