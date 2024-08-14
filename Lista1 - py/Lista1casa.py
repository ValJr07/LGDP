#R = float(input("Quantos reais você quer converter para dolar:"))     #Exercicio 1
#T = R/2.4
#print(T)

#D = float(input("Quantos dolares você vai converter em real:"))       #Exercicio 2 
#T2 = D * 2.4
#print(T2)

#AP = float(input("Qual a altura da parede:"))                              #Exercicio 3
#LP = float(input("Qual a largura da parede:"))                               
#AA = float(input("Qual a altura do azulejo:"))
#LA = float(input("Qual a largura do azulejo:"))
#T = (AP * LP) / (AA * LA)
#print(f"Vai precisa de {T} azulejos")

#h = float(input("Qual a altura do retângulo:"))                        #Exercicio 4
#c = float(input("Qual a comprimento do retângulo:"))
#Area = h * c
#Per = 2 * h + 2 * c
#print(f"Esse é a sua area:{Area}")
#print(f"Esse é o seu perimetro:{Per}")

#M = float(input("Qual a sua massa:"))                                  #Exercicio 5
#H = float(input("Qual a sua altura:"))
#IMC = M / H**2
#print(IMC)

import math

#r = float(input("Qual o valor do raio: "))                             #Exercicio 6
#A = r ** 2 * math.pi
#C = 2 * r * math.pi
#print(f"A sua área é: {A}, e sua comprimento é: {C}")

#R = float(input("Qual o valor do seu raio:"))                          #Exercicio 7
#V = 4/3 * R ** 3 * math.pi
#A = 4 * math.pi * R ** 2
#print(f"Seu volume é: {V}, e sua area é: {A}") 

#pb = float(input("Qual foi sua nota no 1 bimestre:"))                  #Exercicio 8
#sb = float(input("Qual foi sua nota no 2 bimestre:"))
#tb = float(input("Qual foi sua nota no 3 bimestre:"))
#qb = float(input("Qual foi sua nota no 4 bimestre:"))
#NF = (pb + sb + tb + qb)/4
#print(NF)

#P1 = float(input("Qual foi a nota do aluno no 1 semestre:"))           #Exercicio 9
#P2 = float(input("Qual foi a nota do aluno no 2 semestre:"))
#AT = float(input("Qual foi a nota do aluno na atividade:"))
#M = (P1 * 4 + P2 * 4 + AT * 2) /10
#print("Sua nota foi", M)

#a = float(input("Valor de a:"))                                        #Exercicio 10
#b = float(input("Valor de b:"))
#c = a
#a = b
#b = c
#print(f"O valor de a é:{a}\nO valor de b é: {b}")

#a = float(input("Valor de a:"))                                        #Exercicio 11                                   #Exercicio 10
#b = float(input("Valor de b:"))
#a,b = b,a 
#print(f"O valor de a é:{a}\nO valor de b é: {b}")

#D = float(input("Qual foi sua distância:"))                            #Exercicio 12
#T = float(input("Qual foi seu tempo de gasto:"))
#VM = D/T
#print(f"Sua velocidade media foi {VM}")

t = int(input("Qual foi o valor de tempo:"))                           #Exercicio 13
s0 = 2
v0 = 3
a = 10
S = s0 + v0 * t + 1/2 * a * t ** 2
print(f"O resultado é:{S}")