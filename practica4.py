import os
import random

def primerajuste(tambloque,m,tamarch,n):
    allocation = [-1]*n
    for i in range(n):
        for j in range(m):
            if tambloque[j] >= tamarch[i]:
                allocation[i]=j
                tambloque[j] -= tamarch[i]
                break
    print(" Archivo No. TamañoArchivo	 Bloque no.")
    for i in range(n):
        print(" ", i + 1,"          ",tamarch[i],
                        "           ",end = " ")
        if allocation[i] !=-1:
            print(allocation[i]+1)
        else:
            print("No asignado")
    print("Del espacio original de cada bloque, sobro:",tambloque)
    
def mejorajuste(tambloque,m,tamarch,n):
    allocation = [-1] * n
    for i in range(n):
        mejorid = - 1
        for j in range(m):
            if tambloque[j] >= tamarch[i]:
                if mejorid == -1:
                    mejorid = j
                elif tambloque[mejorid] > tambloque[j]:
                    mejorid = j
        if mejorid != -1:
            allocation[i] = mejorid
            tambloque[mejorid] -= tamarch[i]
    print("Archivo No.  TamañoArchivo	   Bloque no.")
    for i in range(n):
        print(i + 1,    "              ", tamarch[i],
                                end =   "             ")
        if allocation[i] != -1:
            print(allocation[i]+1)
        else:
            print("No asignado")
    print("Del espacio original de cada bloque, sobro:",tambloque)
                
def peorajuste(tambloque,m,tamarch,n):
    allocation = [-1] *n
    for i in range(n):
        peorid = -1
        for j in range(m):
            if tambloque[j] >= tamarch[i]:
                if peorid == -1:
                    peorid = j
                elif tambloque[peorid] < tambloque[j]:
                    peorid = j
        if peorid != -1:
            allocation[i] = peorid
            tambloque[peorid] -= tamarch[i]
    print("Archivo No.  TamañoArchivo	Bloque no.")
    for i in range(n):
        print(i + 1,    "               ", 
                    tamarch[i],          end = "       ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("No asignado")
    print("Del espacio original de cada bloque, sobro:",tambloque)
    
def eliminar():
    try:
        for i in range(32):
            i_str=str(i)
            filename='archivo'+i_str+'.txt'
            if os.path.exists(filename):
                os.remove(filename)
            else:
                print("El archivo no existe")
        print("Archivos eliminados")
    except:
        pass
        
array = [1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200,1200]
i=1   
m=len(array) 
lista = []
for i in range(32):
    size = random.randrange(500,1200)
    i_str=str(i)
    filename='archivo'+i_str+'.txt'
    f = open(filename,"w")
    f.seek(size)
    f.write('0')
    f.close()
    for j in range(32):
        filesize = os.path.getsize(filename)  
    lista.append(filesize)
n=len(lista)

entrada=""
print("1.Primer ajuste")
print("2.Mejor ajuste")
print("3.Peor ajuste")
print("4.Eliminar los archivos")
print("5.Salir\n")
while(True):
    entrada = input("Seleccione una opcion: ")
    if entrada  == '1':
        primerajuste(array,m,lista,n)
    elif entrada  == '2':
        mejorajuste(array,m,lista,n)
    elif entrada == '3':
        peorajuste(array,m,lista,n)   
    elif entrada == '4':
        eliminar()   
    elif entrada == '5':
        os.system("cls")
        break
    else:
        print('Error')         


