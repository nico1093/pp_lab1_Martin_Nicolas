import validates



def player_data(players:list, name_player:str) -> dict:
    #Recibe una lista de jugadores y devuelve un jugador.
    #El jugador se encuetra en la lista. 
    #patron_search = r'^{0}$'.format(name_player)
    for player in players:
        if validates.is_player(player,name_player):#re.match(patron_search,player['nombre']):
            return player
        
def search_player(players:list,name_player:str) -> dict:
    #Recibe una lista de jugadores y un nombre de jugador. Devuelve al jugador con ese nombre.
    for player in players:
        if validates.is_player(player, name_player):
            return player
        
def order_players_by_name(players:list) -> list:
    #Recibe una lista de jugadores y los ordena alfabeticamente de forma ascendete.
    aux_players = players
    left_list = []
    rigth_list = []
    if len(aux_players) > 1:
        pivot_player = aux_players[0]
        for player in aux_players[1:]:
            if player['nombre'] < pivot_player['nombre']:
                left_list.append(player)
            else:
                rigth_list.append(player)
    else:
        return aux_players
    left_list = order_players_by_name(left_list)
    left_list.append(pivot_player)
    rigth_list = order_players_by_name(rigth_list)
    left_list.extend(rigth_list)
    return left_list

def the_best_player_statistics_by_key(players:list,key:str) -> dict:
    #Recibe una lista de jugadores y una key. Devuelve al jugador que sobresale en las
    #estadisticas de dicho key. 
    best_player = players[0]
    for player in players[1:]:
        if player['estadisticas'][key] > best_player['estadisticas'][key]:
            best_player = player
    return best_player

def players_exceed_average_by_key(players:list, average:str,key:str) -> list:
    #Recine una lista de jugadores y un promedio y retorna a los jugadores que sobrepasen ese promedio segun
    #la key por partido.
    players_axceed = []
    if validates.is_float_number(average):
        average_points = float(average)
    else:
        average_points = int(average)
    for player in players:
        if average_points <= player['estadisticas'][key]:
            players_axceed.append(player)
    return players_axceed

def order_players_by_statistics_key(players:list,key:str) -> list:
    #Recibe una lista de jugadores y una key de estadisticas y devuelve una lista de forma descendente.
    aux_players = players
    left_list = []
    rigth_list = []
    if len(aux_players) > 1:
        pivot_player = aux_players[0]
        for player in aux_players[1:]:
            if player['estadisticas'][key] > pivot_player['estadisticas'][key]:
                left_list.append(player)
            else:
                rigth_list.append(player)
    else:
        return aux_players
    left_list = order_players_by_statistics_key(left_list, key)
    left_list.append(pivot_player)
    rigth_list = order_players_by_statistics_key(rigth_list, key)
    left_list.extend(rigth_list)
    return left_list
    
def average_statistics_by_key(players:list,key:str) -> float:
    #Recibe una lista de jugadores y una key de estadisticas y devuelve el total de todas las keys.
    #Se usa metodo round para rendondear y validar unicamente hasta dos decimales. 
    total_statistics = 0
    for player in players:
        total_statistics += player['estadisticas'][key]
    return round(total_statistics / len(players),2)

def player_with_more_achievements(players:list) -> dict:
    #Recibe una lista de jugadores y devuelve al jugador que posee mas logros en su carrera.
    more_achievements = players[0]
    for player in players[1:]:
        if len(player['logros']) > len(more_achievements['logros']):
            more_achievements = player
    return more_achievements

'''
DECICION DE APLICACION EJERCICIO 19:
ESTE PUNTO PIDE AL JUGADOR QUE POSEA EL MAXIMO DE TEMPORADAS JUGADAS. COMO EL HECHO QUE HAY 2 JUGADORES 
EN EL SET DE DATOS QUE POSEEN EL MAXIMO DECIDI TRABAJAR CON UNA LISTA DE MAXIMO E IMPRIMIR A TODOS LOS
JUGADORES QUE POSEEN DICHO MAXIMO.
'''
def players_exceed_points_by_position(players:list,average:str,position:str,key:str) -> list:
    #Recibe una lista de jugadores, una promedio de estadisticas, una posicion y una key. Devuelve una lista
    #de los jugadores que cumplen al menos con ese promedio o mas de la key especificada.
    players_exceed = []
    for player in players:
        if position == player['posicion'] and player['estadisticas'][key] >= float(average):
            players_exceed.append(player)
    return players_exceed

def all_positions(players:list) -> list:
    #Recibe una lista de jugadores y devuelve una lista con todas las posiciones que exiten en el equipo.
    positions = []
    for player in players:
        if not(player['posicion'] in positions):
            positions.append(player['posicion'])
    return positions


####### BONUS #######

def player_ranking(players:list, player:str) -> list:
    #Recibe una lista de jugadores y un jugador. Devuelve un lista del jugador con las posiciones del
    #ranking que posee en las estadisticas del equipo.
    ranking_list = [player['nombre']]
    for key in player['estadisticas']:
        ranking_list.append(str(order_players_by_statistics_key(players,key).index(player) + 1))
    return ranking_list