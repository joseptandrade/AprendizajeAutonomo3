Nombre: José Leandro Andrade Zalamea
Fecha: 30/06/2024

Mi proyecto es el Juego de Piedra, papel, tijeras, Spock y Lagarto.

Para este juego necesitamos de dos jugadores los cuales deben ingresar cuantas veces van a jugar y luego de eso elegir las opciones planteadas en el juego Piedra, Papel, Tijeras, Spock o Lagarto dependiendo de lo que elijan el juego va a determinar quien gana, si eligen la misma indicara que es empate, también al finalizar el juego mostrara que jugador gana la partida indicando las veces que haya ganado de igual manera si ganan la misma cantidad de veces indicara que es un empate.

A continuación explico las partes del código cargado en GitHub.

1.	Este comando imprime un mensaje de bienvenida para informar a los jugadores que están iniciando el juego.
print("Bienvenidos al juego de Piedra, Papel, Tijeras, Spock y Lagarto")

2.	Solicitmosa al usuario ingresar cuántas veces desean jugar. El número ingresado se convierte a un entero (`int`) y se almacena en la variable `i`.
i = int(input("Ingrese cuántas veces desean jugar: "))

3.	Inicializamos dos variables `g1` y `g2` en 0. Estas variables se utilizarán para llevar la cuenta de las victorias de cada jugador (`g1` para Jugador 1 y `g2` para Jugador 2).
g1 = 0  # Jugador 1
g2 = 0  # Jugador 2

4.	Definimos un diccionario llamado `opciones` que asigna números enteros del 1 al 5 a las opciones del juego ("Piedra", "Papel", "Tijeras", "Spock", "Lagarto"). Esto facilita la traducción entre la entrada numérica del usuario y la opción textual del juego.
opciones = {
    1: "Piedra",
    2: "Papel",
    3: "Tijeras",
    4: "Spock",
    5: "Lagarto"
}

5.	Iniciamos un bucle `for` que va desde 1 hasta `i` (el número de veces que desean jugar los jugadores). En cada iteración, imprimimos el número de partida usando una cadena de formato (`f-string`).
for numero in range(1, i + 1):
    print(f"\nPartida {numero}:")

6.	Importamos la función `getpass` del módulo `getpass`. Esta función se utiliza para ocultar la entrada de texto mientras el usuario ingresa su elección (lo cual es útil para mantener en secreto la selección del jugador en juegos).
from getpass import getpass

7.	Utilizamos `getpass` para obtener la entrada del usuario de manera oculta (sin mostrar lo que escribe en pantalla). Convertimos la entrada a un entero (`int`) y asigna las elecciones de los jugadores a las variables `j1` y `j2`.
j1 = int(getpass("Jugador 1, elige: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))
j2 = int(getpass("Jugador 2, elige: 1=Piedra, 2=Papel, 3=Tijeras, 4=Spock, 5=Lagarto: "))

8.	Imprime las opciones elegidas por cada jugador, utilizando el diccionario `opciones` para traducir los números (`j1` y `j2`) en las opciones reales del juego.
print(f"Jugador 1 elige: {opciones[j1]}")
print(f"Jugador 2 elige: {opciones[j2]}")

9.	Evalúa quién gana la partida basándose en las reglas del juego. Las combinaciones ganadoras se comparan con las tuplas `(j1, j2)`. Dependiendo de la combinación, se imprime quién ganó la partida o si hubo un empate. Además, se incrementa el contador correspondiente (`g1` o `g2`) según el resultado.
if (j1, j2) in [(1, 2), (1, 4), (2, 3), (2, 5), (3, 1), (3, 4), (4, 2), (4, 5), (5, 1), (5, 3)]:
    print("Jugador 2 gana esta partida.")
    g2 += 1
elif (j1, j2) in [(1, 3), (1, 5), (2, 1), (2, 4), (3, 2), (3, 5), (4, 1), (4, 3), (5, 2), (5, 4)]:
    print("Jugador 1 gana esta partida.")
    g1 += 1
else:
    print("Empate en esta partida.")

10.	Finalmente, imprimimos los resultados finales del juego, mostrando cuántas veces ganó cada jugador (`g1` y `g2`). Luego determinamos quién ganó el juego globalmente o si terminó en empate.
print("\nResultados finales:")
print(f"Jugador 1 ganó {g1} veces.")
print(f"Jugador 2 ganó {g2} veces.")
if g1 > g2:
    print("¡Jugador 1 ha ganado el juego!")
elif g2 > g1:
    print("¡Jugador 2 ha ganado el juego!")
else:
    print("¡El juego terminó en empate!")


