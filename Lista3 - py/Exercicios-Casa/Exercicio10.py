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