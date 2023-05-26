import menu
import main_functions as mf
import files

dream_team = files.read_json('code/PARCIAL/files/dt.json')


while True:   
    match menu.main_menu():
        case 1:
            mf.view_dream_team_players(dream_team)
        case 2:
            mf.view_player_data(dream_team, menu.players_menu())
        case 3:
            player = menu.players_menu()
            mf.import_csv_player_data(player,dream_team,player)
        case 4:
            mf.view_player_achievement(dream_team, menu.players_menu())
        case 5:
            mf.view_average_point_by_order_name(dream_team)
        case 6:
            player = input('Ingrese nombre completo de un jugador... \n')
            mf.view_is_hall_of_fame(dream_team,player)
        case 7:
            mf.view_best_player_statics_by_key(dream_team,'rebotes_totales')
        case 8:
            mf.view_best_player_statics_by_key(dream_team,'porcentaje_tiros_de_campo')
        case 9:
            mf.view_best_player_statics_by_key(dream_team,'asistencias_totales')
        case 10:
            average = input('Ingrese promedio de puntos a validar: ')
            mf.view_max_average_key_by_game(dream_team,average,'promedio_puntos_por_partido')
        case 11:
            average = input('Ingrese promedio de rebotes a validar: ')
            mf.view_max_average_key_by_game(dream_team,average,'promedio_rebotes_por_partido')
        case 12:
            average = input('Ingrese promedio de asistencias a validar: ')
            mf.view_max_average_key_by_game(dream_team,average,'promedio_asistencias_por_partido')
        case 13:
            mf.view_best_player_statics_by_key(dream_team,'robos_totales')
        case 14:
            mf.view_best_player_statics_by_key(dream_team,'bloqueos_totales')
        case 15:
            average = input('Ingrese promedio de porcentaje de libres a validar: ')
            mf.view_max_average_key_by_game(dream_team,average,'porcentaje_tiros_libres')
        case 16:
            mf.view_eleven_best_points(dream_team)
        case 17:
            mf.view_player_with_more_achievements(dream_team)
        case 18:
            average = input('Ingrese promedio de porcentaje de tiros de 3pts a validar: ')
            mf.view_max_average_key_by_game(dream_team,average,'porcentaje_tiros_triples')
        case 19:
            mf.view_players_with_more_seasons(dream_team)
        case 20:
            average = input('Ingrese promedio de tiros de campo a validar: ')
            mf.view_player_order_by_average_key_position(dream_team,average,'porcentaje_tiros_de_campo')
        case 23:
            mf.export_csv_ranking(dream_team)
        case 0:
            print('Fin de proceso...')
            break
