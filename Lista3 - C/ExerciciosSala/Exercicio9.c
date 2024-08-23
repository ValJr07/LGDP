#include <stdio.h>
#include <math.h>
int main() {
    int B, EI, EF;
    printf("Digite sua base: ");
    scanf("%d", &B);
    printf("Digite o valor inicial do seu expoente: ");
    scanf("%d", &EI);
    printf("Digite o valor final do seu expoente: ");
    scanf("%d", &EF);
    for (int x = EI; x <= EF; x++) {

        int t = (int)pow(B, x);
        printf("%d elevado a %d = %d\n", B, x, t);
    }
}
