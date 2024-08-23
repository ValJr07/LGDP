#include <stdio.h>
int main()
{   
    int x,y,t;
    y=0;
    for(x=1;x<=100;++x){
        t=x+y;
        y=t;
    }
    printf("%d\n",t);
}