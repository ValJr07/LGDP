#X = float(input("Digite um numero: "))
#if X % 2 == 0:
#    print("É par")
#else:
#    print("É impar")

#X = int(input("Digite um numero entre 0 e 100: "))
#if X > 100 or X < 0:
#    print("Seu numero não está entre 0 e 100")
#else:
#    T = X - 50
#    if T == 0:
#        print("Achou o numero chave")
#    if T != 0:
#        if T < 0:
#            T2 = T * -1
#            print(f"O numero chaves está {T2} numeros distantes") 
#        else:
#            print(f"O numero chaves está {T} numeros distantes")

#X = float(input("Nota do aluno: "))
#if X % 1 > 0.5:
#    print("Sua nota será", X//1 + 1)
#else:
#    print("Sua nota será", X//1)
'''
x = float(input("Digite um numero X: "))
y = float(input("Digite um numero Y: "))
z = float(input("Digite um numero Z: "))
if x > y and z:
    if y > z:
        print("X é maior\nY é o do meio\nZ o menor")
    if y < z:
        print("X é maior\nZ é o do meio\nY o menor")
    if y == z:
        print("Y e Z são iguais ")
if y > x and z:
    if x > z:
        print("Y é maior\nX é o do meio\nZ o menor")
    if z > x:
        print("Y é maior\nZ é o do meio\nX o menor")
    if x == z:
        print("X e Z são iguais")
if z > x and y:
    if x > y:
        print("Z é maior\nX é o do meio\nY o menor")
    if y > x:
        print("Z é maior\nY é o do meio\nX o menor")
    if x == y:
        print("X e Y são iguais")
if z == x == y:
    print("Os três são iguais")
'''
'''
while True:
    SB = float(input("Qual o seu salario bruto: "))
    if SB == 0:
        break
    H = float(input("Quanto tempo o funcionario trabalhou:"))
    if H <= 160:
        if SB < 800:
            print("Sem desconto")
        else:
            if 800 <= SB <= 1600:
                print("Seu salario liquido é: ", SB - 13/100 * SB)
            else:
                print("Seu salario liquido é: ", SB - 22/100 * SB)
    else:
        if SB < 800:
            t = SB / 160
            t2 = H - 160
            T3 = 50 / 100 * t * t2
            print("Seu salario será: ", SB-T3 )
            exit()
        if 800 <= SB <= 1600:
            print("Seu salario liquido é: ", SB - 13/100 * SB)
        else:
            print("Seu salario liquido é: ", SB - 22/100 * SB)
'''
'''
M = int(input("Digite um numero de 1 ate 12: "))
if M == 1:
    print("Janeiro")
elif M == 2:
    print("Fevereiro")
elif M == 3:
    print("Março")
elif M == 4:
    print("Abril")
elif M == 5:
    print("Maio")
elif M == 6:
    print("Junho")
elif M == 7:
    print("Julho")
elif M == 8:
    print("Agosto")
elif M == 9:
    print("Setembro")
elif M == 10:
    print("Outubro")
elif M == 11:
    print("Novembro")
elif M == 12:
    print("Dezembro") 
else:
    print("Numero não está de 1 até 12")
''' 
'''
N = int(input("Digite o numero de 1 até 5: "))
if N == 1:
    print("Engenharia")
elif N == 2:
    print("Edificações")
elif N == 3:
    print("Sistemas Elétricos")
elif N == 4:
    print("Turismo")
elif N == 5:
    print("Analise de Sistemas")
else:
    print("Numero não está de 1 até 5")
'''
'''
P1 = float(input("Digite o valor da nota do aluno: "))
P2 = float(input("Digite o valor da nota do aluno: "))
P3 = float(input("Digite o valor da nota do aluno: "))
T = (P1 + P2 + P3)/3
if T >= 6:
    print(f"Aprovado e sua nota foi {T}")
else:
    print(f"Reprovado e sua nota foi {T}")
'''
'''
P1 = float(input("Digite o valor da primeira prova: "))    
P2 = float(input("Digite o valor da segunda prova: "))    
T = (P1+P2)/2
if T >= 6:
    print(f"Aprovado, nota: {T}")
else:
    NE = float(input("Qual foi a nota do exame"))
    T2 = (NE + T)/2
    if T2 >= 5:
        print(f"Aprovado, nota: {T2}")
    else:
        print(f"Reprovado, nota: {T2}")
'''
'''
N1 = float(input("Digite um numero: "))
N2 = float(input("Digite um numero: "))
if N1 == N2:
    print("Valores iguais ou seja 0")
    exit()
if N1>N2:
    print("A diferença entre o maior e o menor é: ", N1 - N2)
else:
    print("A diferença entre o maior e o menor é: ", N2 - N1)    
'''
'''
A = int(input("Digite o valor de um lado do triangulo: ")) 
B = int(input("Digite o valor de outro lado do triangulo: "))
C = int(input("Digite o valor de outro lado do triangulo: "))
if A<B+C and B<A+C and C<A+B:
    if A==B!=C or A==C!=B or B==C!=A:
        print("Triangulo isósceles")
    elif A != C and B != C and A != B:
        print("Triangulo escaleno")
    elif A==B==C:
        print("Triangulo equilatero")
'''
'''
A = float(input("Digite um valor: "))
B = float(input("Digite um valor: "))
C = float(input("Digite um valor: "))
if A > B > C:
    print(f"{C},{B},{A}")
if A > C > B:
    print(f"{B},{C},{A}")
if B > A > C:
    print(f"{C},{A},{B}")
if B > C > A:
    print(f"{A},{C},{B}")
if C > A > B:
    print(f"{B},{A},{C}")
if C > B > A:
    print(f"{A},{B},{C}")    
'''
'''
import math
A = int(input("Digite um numero: "))
B = int(input("Digite um numero: "))
C = int(input("Digite um numero: "))
D = B**2 -4*A*C
if D < 0:
    print("Não existe")
X1 = (-B + D**0.5)/2*A
X2 = (-B - D**0.5)/2*A
print(X1, X2)
'''
'''
N = float(input("Digite um valor: "))
if N < 0:
    print(N * -1)
else: 
    print(N)
'''
'''
N1 = int(input("Digite um numero: "))
N2 = int(input("Digite um numero: "))
N3 = int(input("Digite um numero: "))
if N1 % 3 == 0 and N1 % 2 == 0:
    print(N1)
if N2 % 3 == 0 and N2 % 2 == 0:
    print(N2)
if N3 % 3 == 0 and N3 % 2 == 0:
    print(N3)
'''
'''
N1 = int(input("Digite um numero: "))
N2 = int(input("Digite um numero: "))
if N1 % 4 or 5 == 0:
    print(N1)
if N2 % 4 or 5 == 0:
    print(N2)
'''
'''
M = int(input("Digite um numero de 1 ate 12: "))
if M == 1:
    print("Janeiro")
elif M == 2:
    print("Fevereiro")
elif M == 3:
    print("Março")
elif M == 4:
    print("Abril")
elif M == 5:
    print("Maio")
elif M == 6:
    print("Junho")
elif M == 7:
    print("Julho")
elif M == 8:
    print("Agosto")
elif M == 9:
    print("Setembro")
elif M == 10:
    print("Outubro")
elif M == 11:
    print("Novembro")
elif M == 12:
    print("Dezembro") 
else:
    print("Numero não está de 1 até 12")
'''