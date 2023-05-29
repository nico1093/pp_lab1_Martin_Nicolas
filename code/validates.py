import re


def is_int_number(option:str) -> bool:
    #Recibe un string y denota True si la opcion numerica es valida. Caso contrario denota False.
    return re.match(r'^[0-9]+$',option) != None

def is_float_number(number:str) -> bool:
    #Recibe un string y denota True si numero ingresado es decimal. Caso contrario denota False.
    return re.match(r'^[0-9]+.[0-9]+$',number) != None

def is_player(player:dict,player_name:str) -> bool:
    #Recibe un jugadores y el nombre de un jugador. Devuelve True si es el jugador, False en caso contrario.
    return player_name.lower() == player['nombre'].lower()

def validate_name_player(name:str) -> bool:
    #Recibe un nombre y denota True si el nombre es valido. Caso contrario denota False
    #Un nombre tiene el siguiente formato. 1° Nombre y 1° Apellido.
    return re.search(r'^[A-Za-z]+ [A-Za-z]+$',name) != None

def exist_player(players:list,player_name:str) -> bool:
    #Recibe una lista de jugadores y un nombre. 
    #Valida True si existe el jugador con el nombre especificado. Caso contrario valida False
    for player in players:
        if is_player(player,player_name):
            return True
    return False

def validate_hall_of_fame(logros:list) -> bool:
    #Recibe una lista de logros y denota True en caso que dentro de los logros el jugador pertensca al 
    #salon de la fama de baloncesto. Caso contrario denota False.
    #No se considera valida el salon de la Fama de baloncesto Universitario
    for logro in logros:
        if re.search(r'Salon de la Fama del Baloncesto$',logro) != None:
            return True
    return False

def player_is_position(player:dict,position:str) -> bool:
    #Recibe a un jugador y una posicion. Devuelve True en caso que el jugador corresponda a la posicion, 
    #caso contrario denota False.
    #Un jugador es representado con el tipo de dato diccionario.
    return player['posicion'] == position

def info_err_message():
    #Imprime un mensaje al usuario notificando se cometio un error.
    print('ERROR!! Opcion no valida.')

def player_err_message():
    #Imprime un mensaje al usuario notificando que no existe el jugador.
    print('ERROR!! El jugador ingresado no pertenece al Dream Team.')

def data_acces_err_message():
    #Imprime un mensaje al usuario notificando que el dato ingresado no es valido.
    print('ERROR!!! El valor ingresado no corresponde al requerido. Vuelva a intentar.')




