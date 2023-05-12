#condicional 1:

clima = input("llueve? : ")

if (clima == "si" ):
    print("llevar paraguas")
else:
    print("no llevar paraguas")

#condicional 2 : //////////////

user = "name"
pasword = "123"

if (input("ingrese nomre: ") == user ):
    if (input("ingrese pasword: ") == pasword ):
        print("correcto")
    else:
        print("Err1")
else:
    print("Err2")

#condicional 3:

n1 = input("numero 1 ")

n2 = input("numero 2 ")

if (n1>n2):

    print("n1 es mas grande")

else:

    print("n2 es mas grande")

#condicional 4 : 

user_name = input("a) ingrese usuario: ")
user_pasw = input("b) ingrese password: ")

if( user_name == user and user_pasw == pasword ):
    print("ingresado")
else:
    print("Err")


