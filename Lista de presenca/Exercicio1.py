nome = input("Qual seu nome: ")
SA = float(input(f"Salario do {nome}: "))
if 0<SA<=400:
    print(f"Nome do funcionario: {nome}\nAumento foi de: 15%\nSalario atual: {SA}\nNovo salario: {SA+SA*0.15}") 
if 401<=SA<=700:
    print(f"Nome do funcionario: {nome}\nAumento foi de: 12%\nSalario atual: {SA}\nNovo salario: {SA+SA*0.12}") 
if 701<=SA<=1000:
    print(f"Nome do funcionario: {nome}\nAumento foi de: 10%\nSalario atual: {SA}\nNovo salario: {SA+SA*0.10}") 
if 1001<=SA<=1800:
    print(f"Nome do funcionario: {nome}\nAumento foi de: 7%\nSalario atual: {SA}\nNovo salario: {SA+SA*0.07}") 
if 1801<=SA<=2500:
    print(f"Nome do funcionario: {nome}\nAumento foi de: 4%\nSalario atual: {SA}\nNovo salario: {SA+SA*0.04}") 
if SA>2500:
    print("Sem aumento")