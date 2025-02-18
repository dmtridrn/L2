#include<stdlib.h>
#include<stdio.h>
#include<stdbool.h>
#include<time.h>

bool is_in_disk(float x, float y){
    return (x*x + y*y) <= 1;
}

float random_float() {
    return (float)rand() / RAND_MAX;
}

float pi_approx(int n){
    int cpt = 0;
    for(int i = 0; i < n; i++){
        float x = random_float();
        float y = random_float();
        if(is_in_disk(x,y)){
            cpt += 1;
        }
    }
    return 4.0 * cpt/n;
}

int main(){
    srand(time(NULL));
    printf("%f\n", pi_approx(10000000));
}