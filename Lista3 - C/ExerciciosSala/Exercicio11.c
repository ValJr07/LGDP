#include <stdio.h>
int main() {
    int i = 0;
    int num,maior, menor;
    maior = menor = 0;
    printf("Digite 5 números inteiros:\n");
    while (i < 5) {
        printf("Número %d: ", i + 1);
        scanf("%d", &num);
        if (i == 0) {
            maior = menor = num;
        } else {
            if (num > maior) {
                maior = num;
            }
            if (num < menor) {
                menor = num;
            }
        }
        i++;
    }
    printf("O maior número é: %d\n", maior);
    printf("O menor número é: %d\n", menor);
}