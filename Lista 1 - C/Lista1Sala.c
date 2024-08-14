#include <stdio.h>
#include <math.h>
int main(){
    /*
    float d, t, v, lu;
    printf("Digite o tempo gasto: ");
    scanf("%f", &t);
    printf("Digite a velocidade média: ");
    scanf("%f", &v);
    d = t * v;
    lu = d/12;
    printf("A velocidade média foi: %.2f\n", v);
    printf("O tempo foi: %.2f\n", t);
    printf("A distância foi: %.2f\n", d);
    printf("Os litros usados foi: %.2f\n", lu);
    */
    /*
    float f, c;
    printf("Qual é a temperatura em Fahrenheit: ");
    scanf("%f", &f);
    c = (((f - 32)* 5)/9);
    printf("A usa temperatura em centigrados é: %.2f", c);
    */
    /*
    float r, h, v;
    printf("Qual o valor do raio: ");
    scanf("%f", &r);
    printf("Qual a altura: ");
    scanf("%f", &h);
    v = 3.1415 * pow(r, 2) * h;
    printf("Seu volume é: %.2f", v);
    */
    /*
    Exercicio 4
    */
    /*
    int i, t;
    printf("Digite um numero inteiro: ");
    scanf("%i", &i);
    t = pow(i, 2);
    printf("Seu quadrado é: %.2d", t);
    */
    /*
    float v, tp, t ,p;
    printf("Digite o valor: ");
    scanf("%f", &v);
    printf("Digite o tempo: ");
    scanf("%f", &tp);
    printf("Digite o valor da taxa: ");
    scanf("%f", &t);
    p = v +(v * (t/100)* tp);
    printf("O valor da prestação é: %.2f", p);
    */
    int c, t;
    printf("Quantidade de numero de coelhos: ");
    scanf("%i", &c);
    t = (c * 0.7)/18 + 10;
    printf("O custo foi (aproximadamente): %.2i", t);
}