#include <stdio.h>
int main()
{   
    int T, X;
    printf("Digite um numero para saber sua tabuada: ");
    scanf("%d", &T);
    for(X=1;X<11;X+=1){
        printf("%d X %d = %d\n",X,T,X*T);
    }  
}