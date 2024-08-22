B = int(input("Digite sua base: "))
EI = int(input("Digite o valor inicial do seu expoente: "))
EF = int(input("Digite o valor final do seu expoente: "))
for x in range(EI, EF+1, 1):
    t = B ** x
    print(f"{B} elevado a {x} = ",t)