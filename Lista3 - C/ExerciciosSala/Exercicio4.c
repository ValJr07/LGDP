#include <stdio.h>
#include <math.h>
int main()
{   
    int N,t,i;
    printf("Digite um numero: ");
    scanf("%d",&N);
    i=1;
    while(1){
        t=N*pow(3,i);
        if(t<250){
            i+=1;
            printf("%d\n",t);
        }
    }
    
}