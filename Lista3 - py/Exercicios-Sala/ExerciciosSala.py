'''
for x in range(0,20,1):
    if x % 2 != 0:
        print(x)
'''
'''
a1 = int(input("a1: "))
an = int(input("an: "))
Y = 0
print("sn =", ((an + a1) * (an // a1) + 1) // 2)
'''
'''
Y = int(input("Digite um numero para saber sua tabuada: "))
for X in range(1,11,1):
    print(f"{X} X {Y} = ", X*Y)
'''
'''
n = int(input("Digite um numero para saber seu cubo: "))
if n <= 50:
    i = 1
    while True:
        n = n * 3 ** i
        i = i + 1
        if (n >= 250):
            break;
        print (n)
'''
'''
for i in range(1,200,1):
    if i % 4 == 0:
        print(i)
'''
'''
for i in range(15,201,1):
    t = i ** 2
    print(f"{i} ** 2 = ",t)
'''
'''
for i in range(0,16,1):
    t = 3 ** i
    print(f"3 elevado a {i} = ",t)
'''
'''
na = -1
n = 1
for i in range(0,16,1):
    x=n+na
    na=n
    n=x
    if n:
        print(n)
'''
'''
B = int(input("Digite sua base: "))
EI = int(input("Digite o valor inicial do seu expoente: "))
EF = int(input("Digite o valor final do seu expoente: "))
for x in range(EI, EF+1, 1):
    t = B ** x
    print(f"{B} elevado a {x} = ",t)
'''
'''
x = 0
for i in range(1,501,1):
    if i % 2 == 0:
        x += i
print(x)
'''
'''
x=list(map(int,input().split()))
print(max(x),min(x))
'''