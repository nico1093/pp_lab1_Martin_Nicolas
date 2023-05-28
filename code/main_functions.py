import files
import other_functions as of
import validates

def view_dream_team_players(players:list):
    #Recibe una lista de jugadores e imprime por pantalla el nombre y la posicion del jugador
    for player in players:
        print(f'{player["nombre"]} - {player["posicion"]}')



def view_player_data(players:list,name_player:str):
    #Recibe una lista de jugadores y una posicion para imprimir las estadisticas del jugador ubicado en dicha 
    #posicion.
    player = of.player_data(players,name_player)['estadisticas']
    print(f'Nombre: {name_player}')
    for key in player:
        print(f'\t{key.replace("_"," ")}: {player[key]}')

def import_csv_player_data(name_player:str, players:list,name:str):
    #Recibe una lista de jugadores y una posicion para generar un archivo csv con las estadisticas del jugador 
    #ubicado en dicha posicion.
    ruta = f'files/{name_player}.csv'
    player = of.player_data(players,name)['estadisticas']
    data_player = ','.join(player.keys()) + '\n'
    for key in player:
        data_player += str(player[key]) + ','
    files.write_csv_player(ruta,data_player[:-1]) 

def view_player_achievement(players:list, name_player:str):
    #Recibe una lista de jugadores y un nombre de jugador. Imprime por consola los logros de dicho jugador.
    print(f'Logros alcanzado de {name_player}')
    for logros in of.search_player(players,name_player)['logros']:
        print(f'\t-{logros}')

def view_average_point_by_order_name(players:list):
    #Recibe una lista de jugadores e imprime a todos los jugadores con su promedio de puntos.
    for player in of.order_players_by_name(players):
        print(f'Nombre: {player["nombre"]} - Promedio de puntos: {player["estadisticas"]["promedio_puntos_por_partido"]}')

def view_is_hall_of_fame(players:list,name:str):
    #Recibe un nombre y una lista de jugadores, notifica al usuario si ese jugador pertenece al salon de la 
    #fama o no.
    #En caso que no se encuentre el jugador se le notificara mensaje de error al usuario.
    if validates.validate_name_player(name) and validates.exist_player(players,name):
        if validates.validate_hall_of_fame(of.search_player(players,name)['logros']):
            print(f'{name}: Pertenece al Salon de la Fama del Baloncesto')
        else:
            print(f'{name}: No pertenece al Salon de la Fama del Baloncesto')
    else:
        validates.player_err_message()

def view_best_player_statics_by_key(players:list,key:str):
    #Recibe una lista de jugadores y una key. Imprime el nombre del jugador con mas estadisticas totales segun
    #la key especificada.
    player_asist = of.the_best_player_statistics_by_key(players,key)
    print(f'Nombre: {player_asist["nombre"]} - {key.replace("_"," ")}: {player_asist["estadisticas"][key]}')

def view_max_average_key_by_game(players:list, average:str, key:str):
    #Recibe una lista de jugadores y un promedio e imprime a los jugadores que sobrepasan el promedio segun 
    #la key.
    if validates.is_float_number(average) or validates.is_int_number(average):
        if len(of.players_exceed_average_by_key(players,average,key)) > 0:
            for player in of.players_exceed_average_by_key(players,average,key):
                print(f'Nombre: {player["nombre"]} - {key.replace("_"," ")}: {player["estadisticas"][key]}')
        else:
            print('Ningun jugador cumple o sobre pasa dicho promedio.')
    else:
        validates.info_err_message()

def view_eleven_best_points(players:list):
    #Recibe una lista de jugadores e imprime el promedio de puntos por partido de los 11 jugadores con mas
    #anotaciones.
    eleven_best_pointers = of.order_players_by_statistics_key(players,'promedio_puntos_por_partido')[:-1]
    average_points = of.average_statistics_by_key(eleven_best_pointers,'promedio_puntos_por_partido')
    print(f'El promedio de los mejores 11 en puntos convertidos por partido es de: {average_points}')

def view_player_with_more_achievements(players:list):
    #Recibe una lista de jugadores e imprime al jugador con mas logros en su carrera.
    more_achievements = of.player_with_more_achievements(players)
    print(f'Nombre: {more_achievements["nombre"]} - logros: {len(more_achievements["logros"])}')
    print('Los logros:')
    for logro in more_achievements['logros']:
        print(f'\t*{logro}')

def view_players_with_more_seasons(players:list):
    order_seasons = of.order_players_by_statistics_key(players,'temporadas')
    max_seasons = order_seasons[0]['estadisticas']['temporadas']
    for player in order_seasons:
        if max_seasons == player['estadisticas']['temporadas']:
            print(f'nombre: {player["nombre"]} - temporadas: {player["estadisticas"]["temporadas"]}')
        else:
            break


def view_player_order_by_average_key_position(players:list, average:str, key:str):
    #Recibe una lista de jugadores y una promedio de estadisticas y una key. Imprime a los que a los jugadores
    #que superado el promedio de la key especificada y separados por posicion.
    order_players = of.order_players_by_statistics_key(players, key)
    positions = of.all_positions(players)
    for position in positions:
        print(f'\t----- {position} -----\n')
        if len(of.players_exceed_points_by_position(order_players,average,position,key)) > 0: 
            for player in of.players_exceed_points_by_position(order_players,average,position,key):
                print(f'nombre: {player["nombre"]} - posicion: {position} - {key.replace("_"," ")}: {player["estadisticas"][key]}')
            print('\n') #Es un salto de linea para mantener el orden en la consola.
        else:
            print('Los jugadores que juegan en esta posicion no cumplen o superan el porcentaje especificado.\n')    
        
####### BONUS #######

def export_csv_ranking(players:list):
    #Recibe una lista de jugadores y una ruta. Exporta la informacion de todos los jugadores a un archivo
    #con extension csv
    ruta = 'files/dream_team_ranking.csv'
    data_player = 'nombre'
    data_player += ','.join(players[0]['estadisticas'].keys()) + '\n'
    for player in players:
        data_player += ','.join(of.player_ranking(players, player)) + '\n'
    files.write_csv_player(ruta,data_player)            