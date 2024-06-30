print("Bienvenidos al juego de Piedra, Papel, Tijeras, Spock y Lagarto")

# Solicitamos al usuario cuántas veces desea jugar
i = int(input("Ingrese cuántas veces desean jugar: "))

# Inicializamos los contadores de victorias
g1 = 0  # Jugador 1
g2 = 0  # Jugador 2

# Definimos las opciones disponibles y sus respectivos nombres
opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijeras",
    4: "Spock",
    5: "Lagarto"
}

# Iniciamos el bucle de juego para imprimir el numero de Partida
for numero in range(1, i + 1):
    print(f"\nPartida {numero}:")
    
    from getpass import getpass

    # Jugador 1 elige una opción
    j1 = int(getpass("Jugador 1, elige: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))
    
    # Jugador 2 elige una opción
    j2 = int(getpass("Jugador 2, elige: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))
    
    # Mostramos las opciones elegidas por ambos jugadores
    print(f"Jugador 1 elige: {opciones[j1]}")
    print(f"Jugador 2 elige: {opciones[j2]}")
    
    # Evaluamos quién gana esta partida
    if (j1, j2) in [(1, 2), (1, 4), (2, 3), (2, 5), (3, 1), (3, 4), (4, 2), (4, 5), (5, 1), (5, 3)]:
        print("Jugador 2 gana esta partida.")
        g2 += 1
    elif (j1, j2) in [(1, 3), (1, 5), (2, 1), (2, 4), (3, 2), (3, 5), (4, 1), (4, 3), (5, 2), (5, 4)]:
        print("Jugador 1 gana esta partida.")
        g1 += 1
    else:
        print("Empate en esta partida.")
    
# Mostramos los resultados finales del juego
print("\nResultados finales:")
print(f"Jugador 1 ganó {g1} veces.")
print(f"Jugador 2 ganó {g2} veces.")

# Determinamos al ganador del juego o si hubo empate global
if g1 > g2:
    print("¡Jugador 1 ha ganado el juego!")
elif g2 > g1:
    print("¡Jugador 2 ha ganado el juego!")
else:
    print("¡El juego terminó en empate!")
