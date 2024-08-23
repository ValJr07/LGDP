#include <stdio.h>
int main()
{   
    int x,y;
    printf("Digite um numero para saber sua tabuada: ");
    scanf("%d",&y);
    for(x=1;x<=10;x++){
        printf("%d X %d == %d\n", y,x,x*y);
    }
}