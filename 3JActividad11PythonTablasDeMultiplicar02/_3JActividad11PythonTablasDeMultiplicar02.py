#3JEDUARDOVELAZQUEZ
#ACTIVIDAD11
NUM = int(input("Cuantas tablas: "))
t = 1
while t <= NUM:
    i = 10
    while i >= 1:
        RESUL = t * i
        print(f"{t} * {i} = {RESUL}")
        i-=1

    input("Presione enter para continuar...")
    t+=1