#include <stdio.h>
#include <math.h>
int main()
{   
    int n,t;
    for(n=15;n<=200;n++){
        t=pow(n,2);
        printf("%d ** 2 = %d\n",n,t);
    }
}