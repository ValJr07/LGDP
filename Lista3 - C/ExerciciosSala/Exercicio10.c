#include <stdio.h>
#include <math.h>
int main() {
    int x,na,t;
    na=0;
    for(x=1;x<=500;x++){
        if(x%2==0){
            t=x+na;
            na = t;
           
        }
    } printf("%d\n",t);
}
