# condicional 1

num = input("ingrese numero menor a 5 : ")

while ( int(num ) > 5 ) :
    input ("intente de nuevo")
print("valido")

# condicional 2: 

num = input("ingrese valor par: ")

while ( int(num) % 2 ) : 
    input("es impar")
    num = input("ingrese valor par: ")
print("validado")

#millon:

num2 = 1
parra = ""

while ( num2 < 10 ) :
    num2 += 1
    parra = parra + "0" 
print (parra)
print("fin")

# iteracion:

colores = [ "marron","verde","celeste","violeta","naranja","amarillo","azul","rojo", ]
primarios = [ "azul", "amarillo", "rojo" ]
v = True

print("-------colores---------")
for x in colores :
    for p in primarios:
        if x == p : 
            v = False
            break
        else : 
            v = True
    if v :
        print (x)

print("--------primarios--------")

for x in colores :     
    if x in primarios:
        print(x)
print("----------------")


# tupla

my_tupla = ( "A","B","C","D","C", )
print("------tupla-------")
print(my_tupla.index("D"))
print (my_tupla.count("C"))

# diccionario: 

print("----diccionario---------")

persona1 = {
    'name' : 'juan',
    'user_name' : 'pepe',
    'country' : 'AR',
    'age' : 30,
}

print ( "nombre: " + persona1["name"] )

def cambiar_dato (dic):
    key = input("ingrese key del dato: ")
    dic[key] = input ("ingrese dato nuevo: ")

cambiar_dato(persona1)

print (persona1)

print("--------------------")