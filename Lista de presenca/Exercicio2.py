# Lista para armazenar os valores inseridos pelo usuário
v = []

while True:
    entrada = input("Digite um número (ou 'S' para terminar): ")
    
    # Verifica se a entrada é 'S' ou 's'
    if entrada.lower() == 's':
        break
    
    # Tenta converter a entrada para um número e adiciona à lista
    try:
        numero = float(entrada)  # Converte para float para aceitar números decimais
        v.append(numero)  # Adiciona o número à lista
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'S' para terminar.")

# Exibe a lista de números fornecidos
print("Números fornecidos:", v)
