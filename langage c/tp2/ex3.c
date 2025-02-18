#include<stdio.h>
#include<stdlib.h>

int f(int n){
    if(1 == n){
        return 2;
    }
    else{
        return 2*g(n-1);
    }
}

int g(int n){
    if(1 == n){
        return 1;
    }
    else{
        return 3*f(n/2);
    }
}

int main(){
    printf("%i \n", f(20));
}