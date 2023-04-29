'''
En esta actividad se trabaja con listas, 
tuplas y diccionarios. Se manipulan sus propiedades 
como cambio de formato, agregar elementos, seleccionar 
elementos y reordenarlos. Se utilizan ciclos, se trabaja 
con entradas 'input()' y con valores enteros, además se 
utilizan algunas propiedades que no se vieron en el curso 
que fueron investigadas con el proposito de enriquecer este proyecto.
'''
#variables....................0X
#tipos de datos...............0X
#condicionales (if)...........0X
#operadores lógicos...........0X
#listas.......................0X
#iteradores for...............0X
#funciones....................0
#tuplas (no obligatorio)......0X
#diccionarios.................0X

enter1 = []           # entrada del primer vector
while len(enter1) < 3:
  try:
    entrada = int(input ("Ingresa tres valores para formar un vector de tres dimensiones: "))
    enter1.append(entrada)
  except ValueError:            # investigué  como evitar este error para no tener problemas al ingresar mis datos y para tener un proyecto mejor realizado 
    print("Por favor ingresa un número ")
vec1 = tuple(enter1)      # cmabio de formato para convertir la lista en tupla

enter2 = []           # entrada del segundo vector
while len(enter2) < 3:   # uso del ciclo while para admitir unicamente valores numéricos
  try:
    entrada = int(input ("Ingresa tres valores para formar el segundo vector de tres dimensiones: "))
    enter2.append(entrada)
  except ValueError:
    print("Por favor ingresa un número ")
vec2 = tuple(enter2)      # cmabio de formato para convertir la lista en tupla

enter3 = []           # entrada del tercer vector
while len(enter3) < 3:
  try:
    entrada = int(input ("Ingresa tres valores para formar el tercer vector de tres dimensiones: "))
    enter3.append(entrada)
  except ValueError:
    print("Por favor ingresa un número ")
vec3 = tuple(enter3)      # cmabio de formato para convertir la lista en tupla

print(" ")

vectores = [vec1,vec2,vec3]  # una lista de tuplas
matrix = [enter1,enter2,enter3]   # una lista de listas, para este proyecto se utiliza como matríz
matrixT = list(zip(*matrix))      # se investigó esta propiedad para crear la transpuesta y asi calcular el determinante de la matriz segun la fómula clásica
matrixT = [list(t) for t in matrixT]    # la matriz transpuesta de T

propiedades = {"Vectores ":vectores,"Matriz":matrixT}     # se creó un diccionario

det = (matrixT[0][0]*matrixT[1][1]*matrixT[2][2]+matrixT[0][1]*matrixT[1][2]*matrixT[2][0]+matrixT[0][2]*matrixT[1][0]*matrixT[2][1])-(matrixT[2][0]*matrixT[1][1]*matrixT[0][2]+matrixT[2][1]*matrixT[1][2]*matrixT[0][0]+matrixT[2][2]*matrixT[1][0]*matrixT[0][1])     # se calcula el determinante según una fórmula clásica

propiedades["Determinante"] = det     # se agrega el determinate al diccionario

if det == 0:      # se investiga la dependencia o independencia lineal de los vectores introducidos
  propiedades["Dependencia lineal"] = "Los vectores son linealmente dependientes."
else:
  propiedades["Dependencia lineal"] = "Los vectores son linealmente independientes."

for key, values in propiedades.items():
  print(key, "=>", values)
  print(" ")