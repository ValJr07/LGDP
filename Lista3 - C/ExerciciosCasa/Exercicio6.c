#include <stdio.h>
int main()
{   
    int x;
    for(x = 20; x>=1; x--){
        if(x%2==0){
            printf("par = %d\n", x);
        }else{
            printf("impar = %d\n", x);
        }
    }
    
}