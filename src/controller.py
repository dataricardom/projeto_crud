import requests
from db_conn import SessionLocal, engine, Base
from models import Pokemon
from schema import PokemonSchame

Base.metadata.create_all(bind=engine)

def pegar_pokemon(pokemon_id: int) -> PokemonSchame:
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchame(name=data['name'], type=types)
    else:
        return None
    
def add_prokemon_banco(pokemon_schema: PokemonSchame) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon