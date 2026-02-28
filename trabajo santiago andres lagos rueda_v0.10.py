while True:
 e= float(input(" escoja el ejercicio que desea revisar: un programa que convierta un numero binario en decimal. 1 Hacer un programa que solicite un numero y lo invierta sin usar conversion a texto 2 Hacer un programa que genere un vector de numeros aleatorios entre 0 y 100, y luego lo ordene de  mayor a menor y viceversa. Imprimir el vector generado y los vectores ordenados 3 Hacer un programa que llene una matriz de f filas y c columnas, M(f,c) con números aleatorios y la ordene de menor a mayor. Imprimir la matriz sin ordenar y la matriz ordenada.5 Hacer un programa que llene una matriz cuadrada de M(n,n) en forma de caracol. 6 terminar proceso") )
 while e in range(1,6):
    if e not in(1,6):
      print("escoja un numero dentro de las opciones")
    if e==1: 
     binario= input("ingresa un numero binario")
     try:
      decimal= int(binario,2)
      print("el numero decimal es:", decimal)
     except ValueError:
        print(" error ingrese solo caracteres entre 1 y 0")
    if e==2: 
      numero = int(input("ingrese su numero"))
      invertido = 0
      n=abs(numero)
      while n > 0:
       digito= n % 10
       invertido = invertido*10 + digito 
       n = n//10
       if numero<0:
         invertido=-invertido
         print("numero invertido:", invertido)
    if e==3: 
     import random
     cantidad= int(input("¿cuantos numeros desea generar?"))
     vector = [random.randint(1,100) for _ in range(cantidad)]
     ascendente= sorted(vector)
     descendente= sorted(vector, reverse= True)
     print("vector generado")
     print(vector)
     print("ordenado de menor a mayor")
     print(ascendente)
     print("ordenado de mayor a menor")
     print(descendente)
    if e== 4:
      import random
      f=int(input("ingrese el numero de filas"))
      c=int(input("ingrese el numero de columnas"))
      matriz= []
      for i in range(f):
        fila =[]
        for j in range(c):
            fila.append(random.randint(1,100))
      matriz.append(fila)
    print("\nMatriz original:")
    for fila in matriz:
      print(fila)
    elementos=[]
    for fila in matriz:
      for num in fila:
        elementos.append(num)
    elementos.sort()
    matriz_ordenada=[]
    indice=0
    for i in range(f):
      fila=[]
      for j in range(c):
       fila.append(elementos[indice])
       indice+=1
       matriz_ordenada.append(fila)
      print("matriz ordenada de menor a mayor")
      for fila in matriz_ordenada:
        print(fila)            
    if e==5: 
      n=int(input("ingrese e tamaño de la MATRIZ (n)"))
      matriz=[[0]*n for _ in range(n)]
      inicio_fila=0
      fin_fila=n-1
      inicio_col=0
      fin_col=n-1
      num=1
      while inicio_fila<=fin_fila and inicio_col<=fin_col:
        for i in range(inicio_col, fin_col +1):
          matriz[inicio_fila][i] = num
          num+=1
        fin_col-=1
        if inicio_fila<= fin_fila:
          for i in range (fin_col, inicio_col -1,-1):
                