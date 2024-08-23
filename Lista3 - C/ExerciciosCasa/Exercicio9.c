#include <stdio.h>
int main()
{   
    int x;
    x=0;
    do{
        x+=1;
        if(x%2==0){
            printf("par = %d\n",x);
        }else{
            printf("impar = %d\n", x);
        }
    }
    while(x<20);
   
}