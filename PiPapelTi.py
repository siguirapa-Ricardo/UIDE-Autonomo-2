#piedra papel o tijera


contador = 1
ganador1 = 0
ganador2 = 0

print("Hola estas en el juego de Piedra, Papel o Tijera de dos Usuarios")
print("Puedes elegir tu opcion ")
print("Piedra = 1")
print("Papel = 2")
print("Tijera = 3")
while contador <= 3:
    user1 = int(input("Ingrese su opcion Usuario 1: "))
    user2 = int(input("Ingrese su opcion Usuario 2: "))
    if user1 == user2:
        print("Es un empate")
        contador += 1
    else:
        if (user1 == 1 and user2 == 3 ) or (user1 == 2 and user2 == 1 ) or (user1 == 3 and user2 == 2 ):
            ganador1 += 1 
            contador += 1
        else:
            ganador2 +=1
            contador += 1
if ganador1 > ganador2:
    print("El gandor es el usuario 1 ")
else: 
    print("El ganador es el usuario 2 ")