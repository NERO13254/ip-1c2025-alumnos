# capa de transporte/comunicación con otras interfaces o sistemas externos.
import concurrent.futures
import requests
from ...config import config

# comunicación con la API.
def fetch_pokemon(id):
    response = requests.get(config.STUDENTS_REST_API_URL + str(id))
    #  si la respuesta falla
    if not response.ok:
        print(f"[transport.py]: Error")
        return None
    raw_data = response.json()
    return {
        "id": raw_data["id"],
        "name": raw_data["name"],
        "url": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{raw_data['id']}.png",
        "height": raw_data["height"],
        "weight": raw_data["weight"],
        "base": raw_data["base_experience"],
        "types": raw_data["types"],
        "hp": raw_data["stats"][0]["base_stat"]
    }


def getAllImages():
    json_collection = []
    # realiza las consultas a la api al mismo tiempo , reduciendo el tiempo de espera
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_pokemon, range(1,51)))
    json_collection = [r for r in results ]
    return json_collection

# obtiene la imagen correspodiente para un type_id especifico 
def get_type_icon_url_by_id(type_id):
    base_url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2'
    return f"{base_url}{type_id}.png"