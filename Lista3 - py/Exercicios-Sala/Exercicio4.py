n = int(input("Digite um numero: "))
if n <= 50:
    i = 1
    while True:
        n = n * 3 ** i
        i = i + 1
        if (n >= 250):
            break;
        print (n)