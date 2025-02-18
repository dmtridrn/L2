#include<stdlib.h>
#include<stdio.h>
#include<assert.h>
#include<stdbool.h>

struct fraction
{
    long num,den;
};
typedef struct fraction fraction;


fraction build(long n, long d){
    assert(d);
    fraction fr = {.num = n, .den = d};
    return fr;
}

bool eq_fraction(fraction f, fraction g){
    int a = f.num * g.den;
    int b = g.num * f.den;
    return a == b;
}

bool is_int(fraction f){
    return (f.num % f.den == 0);
}

fraction sum(fraction f, fraction g){
    long den_commun = f.den * g.den;
    long num1 = f.num * g.den;
    long num2 = g.num * f.den;
    long sum_num = num1 + num2;
    return build(sum_num, den_commun);
}

fraction sub(fraction f, fraction g){
    long den_commun = f.den * g.den;
    long num1 = f.num * g.den;
    long num2 = g.num * f.den;
    long sub_num = num1 - num2;
    return build(sub_num, den_commun);
}

fraction mul(fraction f, fraction g){
    return build(f.num * g.num, f.den * g.den);
}

long pgcd(long a, long b){
    long x = a;
    long y = b;
    long r = 0;
    while(y!=0){
        r = x%y;
        x = y;
        y = r;
    }
    return x;
}

fraction reduce(fraction f){
    long num = f.num;
    long den = f.den;
    long a = num;
    long b = den;
    if(a<0){
        a = -a;
    }
    if(b<0){
        b = -b;
    }
    long div = pgcd(a,b);
    long nv_num = num/div;
    long nv_den = den/div;
    if((nv_den < 0)){
        nv_num = -nv_num;
        nv_den = -nv_den;
    }
    return build (nv_num,nv_den);
}

void print_fraction(fraction f) {
    printf("%ld/%ld\n", f.num, f.den);
}

int main(){
    fraction fractions[] = {build(1,1),build(1,2),build(2,4),build(-9,3),
    build(8,-20),build(-5,-1),build(1,-3)};
    for(int i = 0; i<7; i++){
        fraction a = reduce(fractions[i]);
        print_fraction(a);
    }
}
