import validates



def main_menu() -> int:
    print('Seleccione al jugador:')
    print('01- Visualizar al Dream Team.')
    print('02- Visualizar estadisticas.')
    print('03- Exportar a CSV estadisticas.')
    print('04- Visualizar logros.')
    print('05- Visualizar jugadores y sus promedio de puntos.(Orden Alfabetico)')
    print('06- Visualizar pertenecia al salon de la fama. (Guiarse con opcion 1)')
    print('07- Visualizar al jugador con mas rebotes totales.')
    print('08- Visualizar al jugador con mayor porcentaje de tiro de campo.')
    print('09- Visualizar al jugador con mas asistencias totales.')
    print('10- Visualizar a los jugadores que superen el promedio de puntos por partidos especificados.')
    print('11- Visualizar a los jugadores que superen el promedio de rebotes por partidos especificados.')
    print('12- Visualizar a los jugadores que superen el promedio de asistencias por partidos especificados.')
    print('13- Visualizar al jugador con mas robos totales.')
    print('14- Visualizar al jugador con mas bloqueos totales.')
    print('15- Visualizar a los jugadores que superen el promedio del porcentaje en tiros libres por partidos especificados.')
    print('16- Visualizar el promedio de puntos por partido de los 11 mayores anotadores.')
    print('17- Visualizar al jugador con mas logros.')
    print('18- Visualizar a los jugadores que superen el promedio del porcentaje en tiros de 3pts por partidos especificados.')
    print('19- Visualizar al/los jugador/es con mas temporadas jugadas.')
    print('20- Visualizar los jugadores que supuren un porcentaje de tiros de campo por posicion.')
    print('23- Exportar ranking de estadisticas del DREAM TEAM.')
    print('00- Salir.')
    option = input()
    if validates.is_int_number(option) and (int(option) <= 20 or int(option) == 23):
        return int(option)
    validates.info_err_message()
    return main_menu()


def players_menu() -> str:
    print('Seleccione al jugador:')
    print('\t1- Michael Jordan')
    print('\t2- Magic Johnson')
    print('\t3- Larry Bird')
    print('\t4- Charles Barkley')
    print('\t5- Scottie Pippen')
    print('\t6- David Robinson')
    print('\t7- Patrick Ewing')
    print('\t8- Karl Malone')
    print('\t9- John Stockton')
    print('\t10- Clyde Drexler')
    print('\t11- Chris Mullin')
    print('\t12- Christian Laettner')
    option = input()
    if validates.is_int_number(option):
        match int(option):
            case 1:
                return 'Michael Jordan'
            case 2:
                return 'Magic Johnson'
            case 3:
                return 'Larry Bird'
            case 4:
                return 'Charles Barkley'
            case 5:
                return 'Scottie Pippen'
            case 6:
                return 'David Robinson'
            case 7:
                return 'Patrick Ewing'
            case 8:
                return 'Karl Malone'
            case 9:
                return 'John Stockton'
            case 10:
                return 'Clyde Drexler'
            case 11:
                return 'Chris Mullin'
            case 12:
                return 'Christian Laettner'
    validates.info_err_message()
    return players_menu()    