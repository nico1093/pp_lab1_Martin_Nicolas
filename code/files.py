import json

def read_json(ruta:str) -> list:
    #Recibe una ruta representado como string y devuelve la lista del dream team
    with open(ruta, 'r') as file:
        players = json.load(file)
    return players['jugadores']


def write_csv_player(ruta:str, data:str):
    #Recibe una ruta e informacion. Y si no existe en la ruta especificada crea el archivo con la data especificada
    #caso contrario la sobre escribe conla nueva data.
    with open(ruta, 'w') as file:
        file.write(data)

