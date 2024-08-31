#include <stdio.h>

int main() {
    char nome[50];
    float salario, novoSalario;
    printf("Qual seu nome: ");
    scanf("%s", nome);
    printf("Salario do %s: ", nome);
    scanf("%f", &salario);
    if (salario > 0 && salario <= 400) {
        novoSalario = salario + salario * 0.15;
        printf("Nome do funcionario: %s\n", nome);
        printf("Aumento foi de: 15%%\n");
        printf("Salario atual: %.2f\n", salario);
        printf("Novo salario: %.2f\n", novoSalario);
    } else if (salario >= 401 && salario <= 700) {
        novoSalario = salario + salario * 0.12;
        printf("Nome do funcionario: %s\n", nome);
        printf("Aumento foi de: 12%%\n");
        printf("Salario atual: %.2f\n", salario);
        printf("Novo salario: %.2f\n", novoSalario);
    } else if (salario >= 701 && salario <= 1000) {
        novoSalario = salario + salario * 0.10;
        printf("Nome do funcionario: %s\n", nome);
        printf("Aumento foi de: 10%%\n");
        printf("Salario atual: %.2f\n", salario);
        printf("Novo salario: %.2f\n", novoSalario);
    } else if (salario >= 1001 && salario <= 1800) {
        novoSalario = salario + salario * 0.07;
        printf("Nome do funcionario: %s\n", nome);
        printf("Aumento foi de: 7%%\n");
        printf("Salario atual: %.2f\n", salario);
        printf("Novo salario: %.2f\n", novoSalario);
    } else if (salario >= 1801 && salario <= 2500) {
        novoSalario = salario + salario * 0.04;
        printf("Nome do funcionario: %s\n", nome);
        printf("Aumento foi de: 4%%\n");
        printf("Salario atual: %.2f\n", salario);
        printf("Novo salario: %.2f\n", novoSalario);
    } else if (salario > 2500) {
        printf("Sem aumento\n");
    }

    return 0;
}
