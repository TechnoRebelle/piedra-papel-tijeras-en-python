nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

jugador1 = input("¡hola " + nombre1 + " ¿Que elijes? ¿Piedra, papel o tijeras: ")
jugador2 = input("¡hola " + nombre2 + " ¿Que elijes? ¿Piedra, papel o tijeras: ")


jugador1_lower = jugador1.lower()
jugador2_lower = jugador2.lower()


condicion1 = jugador1_lower == "piedra" and jugador2_lower == "tijeras"
condicion2 = jugador1_lower == "papel" and jugador2_lower == "piedra"
condicion3 = jugador1_lower == "tijeras" and jugador2_lower == "papel"

if jugador1_lower == jugador2_lower:
    print("Ha sido un empate")
elif condicion1 or  condicion2 or condicion3 :
    print("Ha ganado ", nombre1)

else:
    print("Ha ganado ", nombre2)









