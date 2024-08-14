#include <stdio.h>
#include <math.h>
int main(){
    
    /*
    float R;                                        
    float D;
    printf("Qual o valor em reais:");
    scanf("%f", &R);
    D = R/2.4;
    printf("Valor em dolares é:  %.2f", D);
    return 0;
    */
    
    /*
    float R, D;                                     
    printf("Qual o seu valor em dolares:"); 
    scanf("%f", &D);
    R = D * 2.4;
    printf("Seu valor em reais é: %.2f", R);
    */
    /*
    float T, AP, LP, AA, LA;
    printf("Qual é a altura da parede: ");
    scanf("%f", &AP);
    printf("Qual é a largura da parede: ");
    scanf("%f", &LP);
    printf("Qual é a altura do azulejo: ");
    scanf("%f", &AA);
    printf("Qual é a largura do azulejo: ");
    scanf("%f", &LA);
    T = (AP * LP) / (LA * AA);
    printf("O total de azulejo necessario será: %.2f", T);
    */
    /*
    float h, c, A, P;
    printf("Qual a altura do retângulo: ");
    scanf("%f", &h);
    printf("Qual o comprimento do rentângulo: ");
    scanf("%f", &c);
    A = h * c;
    P = 2 * h + 2 * c;
    printf("Esse é a sua area: %.2f", A);
    printf("E Esse o seu perimetreo: %.2f", P);
    */
    /*
    float M, H, IMC;
    printf("Qual sua massa: ");
    scanf("%f", &M);
    printf("Qual a sua altura: ");
    scanf("%f", &H);
    IMC = M / pow(H, 2);
    printf("Seu IMC será: %.5f", IMC);
    */
    /*
    float r, A, C;
    printf("Qual o valor do raio: ");
    scanf("%f", &r);
    A = pow(r, 2) * 3.1415;
    C = r * 2 * 3.1415;
    printf("Sua area é: %.2f", A);
    printf("E seu perimetro é: %.2f", C);
    */
    /*
    float R, V, A;
    printf("Qual o valor do seu raio: ");
    scanf("%f", &R);
    V = 1.333 * pow(R, 3) * 3.1415;
    A = 4 * 3.1415 * pow(R, 2);
    printf("Seu volume é: %.2f", V);
    printf("Sua area é: %.2f", A);
    */
    /*
    float sb, pb, tb, qb, NF;
    printf("Qual foi sua nota no 1 bimestre: ");
    scanf("%f", &pb);
    printf("Qual foi sua nota no 2 bimestre: ");
    scanf("%f", &sb);
    printf("Qual foi sua nota no 3 bimestre: ");
    scanf("%f", &tb);
    printf("Qual foi sua nota no 4 bimestre: ");
    scanf("%f", &qb);
    NF = (pb + sb + tb + qb)/4;
    printf("Sua nota foi: %.2f", NF);
    */
    /*
    float P1, P2, AT, M;
    printf("Qual foi a nota no 1 semestre: ");
    scanf("%f", &P1);
    printf("Qual foi a nota no 2 semestre: ");
    scanf("%f", &P2);
    printf("Qual foi a nota do aluno na atividade: ");
    scanf("%f", &AT);
    M = (P1 * 4 + P2 * 4 + AT * 2)/10;
    printf("Sua nota foi: %.2f", M);
    */
    /*
    float a, b, c;
    printf("Valor de a: ");
    scanf("%f", &a);
    printf("Valor de b: ");
    scanf("%f", &b);
    c = a;
    a = b;
    b = c;
    printf("O valor de a virou: %.2f \n", a);
    printf("O valor de b virou: %.2f \n", b);
    */
    /*
    float a, b;
    printf("Valor de a: ");
    scanf("%f", &a);
    printf("Valor de b: ");
    scanf("%f", &b);
    a, b = b, a;
    printf("O valor de a é: %.2f\n", a);
    printf("O valor de b é: %.2f\n", b);
    */
    /*
    float d, t, vm;
    printf("Qual foi sua distância: ");
    scanf("%f", &d);
    printf("Qual foi seu tempo gasto: ");
    scanf("%f", &t);
    vm = d/t;
    printf("Sua velocidade média foi: %.2f", vm);
    */
    /*
    float t, s;
    printf("Qual foi o valor de tempo: ");
    scanf("%f", &t);
    s = 2 + 3 * t + 0.5 * 10 * pow(t, 2);
    printf("O resultado é: %.2f", s);
    */
}