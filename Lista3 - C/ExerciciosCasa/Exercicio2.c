#include <stdio.h>
int main()
{   
    int x;
    x = 0;
    while(x<20){
        x=x+1;
        if(x%2==0){
            printf("%d\n",x);
        }
    }
}