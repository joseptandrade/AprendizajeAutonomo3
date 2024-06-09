
###Juego de Piedra, Papel, Tijeras, Spock y Lagarto

###Imprimimos un mensaje de Bienvenida
print("Bienvenidos al juego de Piedra, Papel, Tijeras, Spock y Lagarto")

###Solicitamos al usuario ingrese cuantas veces desea jugar y lo guardamos en la variable i
i = int(input("Ingresen cuantas veces desean jugar: "))

##Inicializamos la variable con la que vamos a comparar la variable i
numero = 1
###Variables para el ganador de la partida
g1 = 0
g2 = 0

###Iniciamos nuestro bucle comparando la variable número si es menor o igual
###Si se cumple ingresamos al bucle
while numero <= i:
    ###A la variable numero la vamos incrementando en uno para luego realizar la comparación al inicio del bucle
    numero += 1
    ###Pedimos a los jugadores ingresar la opción que van a elegir 
    j1 = int(input("Jugador 1 Ingrese una de las siguientes opciones: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))
    j2 = int(input("Jugador 2 Ingrese una de las siguientes opciones: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))
    ###Iniciamos las condicionales para cada opción de ingreso, al cumplirse se imprime mensaje con el número del jugador que gane 
    ##Comparamos los posibles ingresos para la opción 1 que es Piedra
    if j1 == 1 and j2 == 2:
            print("Jugador 2 Gana: Papel gana a Piedra")
            g2 +=1
    elif j1 == 1 and j2 == 3:
            print("Jugador 1 Gana: Piedra gana a Tijeras")
            g1 +=1
    elif j1 == 1 and j2 == 4:
            print("Jugador 2 Gana:  Spock gana a Piedra")
            g2 +=1
    elif j1 == 1 and j2 == 5:
            print("Jugador 1 Gana: Piedra gana a Lagarto")
            g1 +=1
    ##Comparamos los posibles ingresos para la opción 2 que es Papel
    elif j1 == 2 and j2 == 1:
            print("Jugador 1 Gana: Papel gana a Piedra")    
            g1 +=1
    elif j1 == 2 and j2 == 3:
            print("Jugador 2 Gana: Tijera gana a Papel")
            g2 +=1
    elif j1 == 2 and j2 == 4:
            print("Jugador 1 Gana: Tijera gana a Papel")
            g1 +=1
    elif j1 == 2 and j2 == 5:
            print("Jugador 2 Gana: Lagarto gana a Papel")
            g2 +=1
    ##Comparamos los posibles ingresos para la opción 3 que es Tijeras
    elif j1 == 3 and j2 == 1:
        print("Jugador 2 Gana: Piedra gana a Tijeras") 
        g2 +=1
    elif j1 == 3 and j2 == 2:
        print("Jugador 1 Gana: Tijera gana a Papel") 
        g1 +=1
    elif j1 == 3 and j2 == 4:
        print("Jugador 2 Gana: Spock gana a Tijera")
        g2 +=1
    elif j1 == 3 and j2 == 5:
        print("Jugador 1 Gana: Tijera gana a Lagarto")
        g1 +=1
    ###Comparamos los posibles ingresos para la opción 4 que es Spock
    elif j1 == 4 and j2 == 1:
        print("Jugador 1 Gana:  Spock gana a Piedra")
        g1 +=1
    elif j1 == 4 and j2 == 2:
        print("Jugador 2 Gana: Tijera gana a Papel")
        g2 +=1
    elif j1 == 4 and j2 == 3:
        print("Jugador 1 Gana: Spock gana a Tijera")    
        g1 +=1
    elif j1 == 4 and j2 == 5:
        print("Jugador 2 Gana: Lagarto gana a Spock")
        g2 +=1
    ###Comparamos los posibles ingresos para la opción 5 que es lagarto
    elif j1 == 5 and j2 == 1:
        print("Jugador 2 Gana: Piedra gana a Lagarto")
        g2 +=1
    elif j1 == 5 and j2 == 2:
        print("Jugador 1 Gana: Lagarto gana a Papel")
        g1 +=1
    elif j1 == 5 and j2 == 3:
        print("Jugador 2 Gana: Tijera gana a Lagarto")
        g2 +=1
    elif j1 == 5 and j2 == 4:
        print("Jugador 1 Gana: Lagarto gana a Spock")
        g1 +=1
    else:
        ###En caso de no cumplirse las condiciones se imprime lo siguiente
        print("Jugadores quedaron empate")
### Comparamos si el contador g1 es mayor que g2 si se cumple la condición se imprime lo siguiente
if g1 > g2:
     print("Jugador 1 has ganado", g1 ,"veces la partida")
     print("Eres el ganador de la partida, el juego a terminado gracias")
### Comparamos si el contador g2 es mayor que g1 si se cumple la condición se imprime lo siguiente
elif g2 > g1:
    print("Jugador 2 has ganado", g2 ,"veces la partida")
    print("Eres el ganador de la partida, el juego a terminado gracias")
###Caso contrario se imprime el empate 
else:
     print("Empataron la partida, el juego a terminado gracias")