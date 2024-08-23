#include <stdio.h>
#include <stdbool.h>
int main()
{   
    char OP;
    float A,B;
    while (true){
        printf("Digite alguma operação aritmética('+','-','*','/' ou 'S' - Sair): ");
        scanf(" %c", &OP);
        if(OP == 'S'){
            break;
        }
        printf("Digite o primeiro numero: ");
        scanf("%f", &A);
        printf("Digite o segundo numero: ");
        scanf("%f", &B);
        switch(OP){
            case '+':
                printf("%.2f\n",A+B);
                break;
            case '-':
                printf("%.2f\n",A-B);
                break;
            case '*':
                printf("%.2f\n",A*B);
                break;
            case '/':
                printf("%.2f\n",A/B);
                break;
        }
    }
}