for i in range (1,-11,-1):
    print(i)
 
print("ptograma 2")
i =10   
while i >=-10:
    print(i)
    i=i-2

print("ejercicio 1")

while True:
    try:
        numero= float(input(" ingresa un numero ") )
        break   
    except ValueError:
       print("error, ingresa un numero valido")
while True:
    try:
        numero2= float(input(" ingresa un segundo numero ") )
        break   
    except ValueError:
       print("error, ingresa un numero valido")       
print("tu numero es ",numero,numero2) 
e= float(input(" que operacion desea hacer? 1 es para suma,  2 es para resta, 3 es para multiplicacion, 4 es para division, 5 es para finalizar") )
while e in range(1,6):
    if e not in(1,6):
        print("escoja un numero dentro de las opciones")
    if e==1: 
     resultado=numero+numero2
    print("la suma es:",resultado)
    if e==2: 
     resultado=numero-numero2
    print("la resta es:",resultado)
    if e==3: 
     resultado=numero*numero2
    print("la multplicacion es:",resultado)
    if e==4: 
     resultado=numero/numero2
    print("la division es:",resultado)
    if e==5: 
     exit
