#include <stdio.h>
int main(){
    /*
    int x;
    for(x = 0;x<=20;x = x + 1){
        if(x % 2 != 0){
            printf("%d\n", x);
        }
    }
    */

    /*
    int N2 = 0;
    for(int N = 1; N<=100; N+=1){
        N2 += N; 
    }
    printf("%d\n", N2);
    return 0;
    */

   printf("Numero que voce quer saber a tabuada: ");
   scanf("%f", int N2);
   for(int N1 = 1; N1<=10;N1+=1){
        printf(N2, "X", N1, "\n");
   }
}