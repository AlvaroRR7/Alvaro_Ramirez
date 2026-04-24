
can=input("ingrese el nombre del candidato: ")
can2=input("ingrese el nombre del siguiente candidato: ")
v1=0
v2=0
votantes=int(input("ingrese la cantidad de votantes: "))
for i in range(votantes):
    voto=int(input(f"por quien votara. 1.-{can} 2.- {can2} "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print ("voto no valido")
        if v1>v2 