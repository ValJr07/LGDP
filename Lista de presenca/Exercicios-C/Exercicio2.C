#include <stdio.h>

int main() {
    int l[1000];
    int c = 0;  
    int N;
    char s[10];
    while (1) {
        printf("Sair(Digite 'Sair', senao digite qualquer caractere): ");
        scanf("%s", s);
        if (s[0] == 'S' && s[1] == 'a' && s[2] == 'i' && s[3] == 'r' && s[4] == '\0') {
            break;
        }
        while (1) {
            printf("Digite um número (0 para parar): ");
            scanf("%d", &N);

            if (N == 0) {
                break;
            }
            l[c] = N;
            c++;
        }
        if (c > 0) {
            int sum = 0;
            int max = l[0];
            int min = l[0];
            for (int i = 0; i < c; i++) {
                sum += l[i];
                if (l[i] > max) {
                    max = l[i];
                }
                if (l[i] < min) {
                    min = l[i];
                }
            }
            float average = (float)sum / c;
            printf("a) R: %.2f\n", average);
            printf("b) R: max = %d, min = %d\n", max, min);
            int cf1 = 0, cf2 = 0, cf3 = 0, cf4 = 0, cf5 = 0;
            for (int i = 0; i < c; i++) {
                if (l[i] < 0) {
                    cf1++;
                    printf("Faixa 1 - Elementos < 0: %d\n", l[i]);
                } else if (l[i] >= 0 && l[i] < 15) {
                    cf2++;
                    printf("Faixa 2 – Elementos >= 0 e < 15: %d\n", l[i]);
                } else if (l[i] >= 15 && l[i] < 100) {
                    cf3++;
                    printf("Faixa 3 – Elementos >= 15 e < 100: %d\n", l[i]);
                } else if (l[i] >= 1000) {
                    cf4++;
                    printf("Faixa 4 – Elementos >= 1000: %d\n", l[i]);
                } else if (l[i] >= 101 && l[i] < 1000) {
                    cf5++;
                    printf("Faixa 5 – Elementos >= 101 e < 1000: %d\n", l[i]);
                }
            }
            printf("Quantidade de elementos na faixa 1 (< 0): %d\n", cf1);
            printf("Quantidade de elementos na faixa 2 (>= 0 e < 15): %d\n", cf2);
            printf("Quantidade de elementos na faixa 3 (>= 15 e < 100): %d\n", cf3);
            printf("Quantidade de elementos na faixa 4 (>= 1000): %d\n", cf4);
            printf("Quantidade de elementos na faixa 5 (>= 101 e < 1000): %d\n", cf5);
            int contp = 0, conti = 0;
            for (int i = 0; i < c; i++) {
                if (l[i] % 2 == 0) {
                    printf("%d é par\n", l[i]);
                    contp++;
                } else {
                    printf("%d é ímpar\n", l[i]);
                    conti++;
                }
            }
            printf("Quantidade de números pares: %d\n", contp);
            printf("Quantidade de números ímpares: %d\n", conti);
        }
    }
}
