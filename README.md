Mi proyecto es el Juego de Piedra, papel, tijeras, Spock y Lagarto.

Para este juego necesitamos de dos jugadores los cuales deben ingresar cuantas veces van a jugar y luego de eso elegir las opciones planteadas en el juego Piedra, Papel, Tijeras, Spock o Lagarto dependiendo de lo que elijan el juego va a determinar quien gana, si eligen la misma indicara que es empate, también al finalizar el juego mostrara que jugador gana la partida indicando las veces que haya ganado de igual manera si ganan la misma cantidad de veces indicara que es un empate.

A continuación explico las partes del código cargado en GitHub.

1. El juego comienza con un mensaje de bienvenida al juego.

2. Luego el juego pide cuantas veces desean jugar 

3. Inicializamos variables que vamos a usar para identificar al ganador de la partida y para guardar las veces que vamos a jugar 

4. Iniciamos el bucle  comparando si la variable ingresada por el usuario es menor a nuestra variable numero, el jugador al menos debe ingresar 1 para jugar caso contrario se finaliza imprimiendo "El juego a terminado gracias"

5. Ingresando al bucle se va a incrementando nuestro contador numero para guardar las veces que se ha jugado.

6. Pedimos a los jugadores que ingresen la opción que desean para empezar el juego.

7. Iniciamos con los condicionales comparando todas las opciones posibles que los jugadores puedan ingresar y de esa manera identificar al ganador imprimiendo un mensaje "Jugador 2 Gana: Papel gana a Piedra" para este caso el Jugador 1 debió ingresar 1 y el Jugador 2 ingreso 2 de esta manera se cumple la condición y se imprime el mensaje.

8. Si ambos ingresan lo mismo se imprime "Jugadores quedaron empate"

9. Tengo otro condicional comparando las variables del contador para establecer al ganador de la partida al cumplirse una de las condiciones se imprime el mensaje indicando que jugador es el ganador y cuantas veces a ganado.

10. Al no cumplirse se imprime que empataron.  
