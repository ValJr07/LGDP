#include <stdio.h>
#include <math.h>
int main()
{   
    int c,na,np,t;
    na=-1;
    np=1;
    for(c=0;c<=15;c++){
        t = na+np;
        na=np;
        np=t;
        printf("%d\n",t);
    }
}