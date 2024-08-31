l=[]
c=0
while True:
    s = input("Sair(Digite 'Sair', senao digite qualquer caractere): ")
    if s == 'Sair':
        break
    while True:
        N = int(input())
        if N == 0:
           break
        c+=1
        l.append(N)
    print(f"a)R: {sum(l)/c}")
    print(f"b)R: {max(l),min(l)}")
    cf1 = cf2 = cf3 = cf4 = cf5 = 0
    for i in l:
        if i < 0:
            cf1 += 1
            print(f"Faixa 1 - Elementos < 0: {i}")
        elif i >= 0 and i < 15:
            cf2 += 1
            print(f"Faixa 2 – Elementos >= 0 e < 15: {i}")
        elif i >= 15 and i < 100:
            cf3 += 1
            print(f"Faixa 3 – Elementos >= 15 e < 100: {i}")
        elif i >= 1000:
            cf4 += 1
            print(f"Faixa 4 – Elementos >= 1000: {i}")
        elif i >= 101 and i < 1000: 
            cf5 += 1
            print(f"Faixa 5 – Elementos >= 101 e < 1000: {i}")
    print(f"Quantidade de elementos na faixa 1 (< 0): {cf1}")
    print(f"Quantidade de elementos na faixa 2 (>= 0 e < 15): {cf2}")
    print(f"Quantidade de elementos na faixa 3 (>= 15 e < 100): {cf3}")
    print(f"Quantidade de elementos na faixa 4 (>= 1000): {cf4}")
    print(f"Quantidade de elementos na faixa 5 (>= 101 e < 1000): {cf5}")
    contp=0
    conti=0
    for i in l:
        if i%2==0:
            print(f"{i} é par")
            contp+=1
        else:
            print(f"{i} é impar")
            conti+=1
    print(f"Quantidade de numeros pares: {contp}")
    print(f"Quantidade de numeros impares: {conti}")