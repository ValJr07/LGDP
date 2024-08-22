'''
x = 1
while(x<=20):
    print(x)
    x+=1
'''
'''
X = 1
while(X<20):
    if X % 2 == 0:
        print(X)
    X+=1
'''
'''
X = 1
while(X<=20):
    if X%2==0:
        print(f"{X} é par")
    else:
        print(f"{X} é impar")
    X+=1
'''
'''
for X in range(1,20,1):
    print(X)
'''
'''
for X in range(2,19,1):
        if X % 2 != 0:
            print(X)
'''
'''
for X in range(1,20,1):
    if X % 2 == 0:
        print(f"{X} é par")
    else:    
        print(f"{X} é impar")
'''
'''
x = 1
while(x<=20):
    print(x)
    x+=1
'''
'''
X = 1
while(X<20):
    if X % 2 == 0:
        print(X)
    X+=1
'''
'''
X = 1
while(X<=20):
    if X%2==0:
        print(f"{X} é par")
    else:
        print(f"{X} é impar")
    X+=1
'''
'''
while True:
    OP = input("Digite alguma operação aritmética('+','-','*','/' ou 'S' - Sair): ")
    if OP == "S":
        break
    A = float(input("Digite o primeiro numero: "))
    B = float(input("Digite o segundo numero: "))
    if OP == "+":
        print(A+B)       
    elif OP == "-":
        print(A-B)       
    elif OP == "*":
        print(A*B)
    elif OP == "/":
        print(A/B)
'''
'''
T = int(input("Digite um numero para saber sua tabuada: "))
for X in range(1,11,1):
    print(f"{X} x {T} =", X * T)
'''