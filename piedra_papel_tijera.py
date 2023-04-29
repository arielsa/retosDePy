import random
#variables....................0X
#tipos de datos...............0X
#condicionales (if)...........0X
#operadores lógicos...........0X
#listas.......................0
#iteradores for...............0
#funciones....................0x
#tuplas (no obligatorio)......0X
#diccionarios.................0

options = ("piedra", "papel", "tijeras")

nombre = input("¿Cuál es tu nombre? ")
user_win = 0
computer_win = 0
ronda = 1
wins = 0

def ganador(computer, user,name,):    
    if user == 2:
      print("Con un marcador de 2 a ", computer)
      print ('GANO ' + name + '!')
    if computer == 2:
      print("Con un marcador de 2 a ", user)
      print("GANO LA COMPUTADORA!")

while wins == 0  :
  print ('*'*10)
  print ("Ronda", ronda)
  print ('*'*10)
  print (nombre, " = ", user_win, "VS Computadora = ", computer_win)

  user_op = input(nombre + " elige: piedra, papel o tijeras? ")
  user_op = user_op.lower()

  while user_op not in options:
      print(user_op, " no es una opción válida")
      user_op = input(nombre + " vuelve a intentar, elige: piedra, papel o tijeras? ")
      if user_op in options:
        break
      
  computer_op=random.choice(options)
  ronda +=1
  
  print("La computadora eligió", computer_op)
  
  if user_op == computer_op:
    print("Es un empate!")
  elif user_op == "piedra":
    if computer_op == "tijeras":
      print("Piedra gana a tijeras")
      print("Gano " + nombre + "!")
      user_win += 1
    else:
      print("Papel gana a piedra")
      print("Gano la computadora!")
      computer_win += 1
  elif user_op == "papel":
    if computer_op == "piedra":
      print("Papel gana a piedra")
      print("Gano " + nombre + "!")
      user_win += 1
    else:
      print("Tijeras gana a papel")
      print("Gano la computadora!")
      computer_win += 1
  elif user_op == "tijeras":
    if computer_op == "papel":
      print("Tijeras gana a papel")
      print("Gano " + nombre + "!")
      user_win += 1
    else:
      print("Piedra gana a tijeras")
      print("Gano la computadora!")
      computer_win += 1
  
  if user_win == 2 or computer_win == 2 :
    ganador(computer_win,user_win,nombre)
    wins=1
    break



