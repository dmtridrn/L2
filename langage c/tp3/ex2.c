#include<stdlib.h>
#include<stdio.h>

#define N 100

struct polynome
{
    int de;
    int co[N];
};
typedef struct polynome polynome;

int eval(polynome p, int x){
    int res = 0;
    for(int i = p.de; i>=0; --i){
        res = res * x + p.co[i];
    }
    return res;
}

void print_poly(polynome p){
    for(int i = p.de; i>=0; --i){
        if(!p.co[i] == 0){
            if(i == p.de){
                printf("%iX^%i",p.co[i],i);
            }
            else if(i == 1){
                printf(" + %iX",p.co[i]);
            }
            else if(i == 0){
                printf(" + %i",p.co[i]);
            }
            else{
                printf(" + %iX^%i",p.co[i],i);
            }
        }
    }
    printf("\n");
}

polynome derive(polynome p){
    for(int i = 0; i<=p.de; ++i){
        p.co[i] = p.co[i+1] * (i+1);
        
    }
    p.de--;
    return p;
}

polynome add(polynome p1, polynome p2){
    polynome res;
    int degre = 0;

    if(p1.de >= p2.de){
        degre = p1.de;
    }
    else{
        degre = p2.de;
    }
    res.de = degre;
    for(int i = 0; i<=degre; i++){
        res.co[i] = p1.co[i] + p2.co[i];
    }
    return res;
}

void init_poly_zero(polynome *p) {
    //rend tous les coeff de p = 0
    for (int i = 0; i < N; ++i) {
        p->co[i] = 0;
    }
    p->de = 0;
}

polynome times_coeff(polynome p, int coeff, int degre){
    polynome res;
    init_poly_zero(&res);
    res.de = p.de + degre;
    for(int i = 0; i <= p.de; i++){
        res.co[i + degre] = p.co[i] * coeff;
    }
    return res;
}

polynome times(polynome p, polynome q){
    polynome temp;
    polynome res;
    res.de = p.de + q.de;
    init_poly_zero(&res);
    for(int i = 0; i <= p.de; i++){
        temp.de = q.de + i;
        init_poly_zero(&temp);
        temp = times_coeff(q, p.co[i], i);
        res = add(res, temp);
    }
    return res;
}

int main(){
    polynome p;
    p.de = 2;
    p.co[0] = 1;
    p.co[1] = 4;
    p.co[2] = 2;
    polynome q;
    q.de = 2;
    q.co[0] = 2;
    q.co[1] = 3;
    q.co[2] = 3;
    print_poly(p);
    print_poly(q);
    print_poly(times(p,q));
    
    
}