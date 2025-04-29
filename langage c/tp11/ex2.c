#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>
#include <stddef.h>


typedef struct {
    void *first;
    void *last;
    size_t te;
    void *occupe;
    void *libre;
} fifo;

static void *decale(void *f, size_t d){
    return ((char*)f) + d;
}

static ptrdiff_t diff(void *f, void *g){
    return ((char*)g) - ((char*)f);
}

fifo *create_fifo(size_t capacite, size_t te){
    fifo *pf = malloc(sizeof(fifo));
    assert(pf != NULL);
    void *res = malloc(capacite * te);
    assert(res != NULL);
    pf->te = te;
    pf->first = pf->libre = pf->occupe = res;
    pf->last = decale(res, capacite * te);
    return pf;
}

void delete_fifo(fifo *f){
    free(f->first);
    free(f);
}

int empty_fifo(fifo *f){
    if(f->occupe == f->libre){
        return 1;
    }
    return 0;
}

void *get_fifo(fifo *f, void *element){
    if(empty_fifo(f)){
        return NULL;
    }
    memmove(element, f->occupe, f->te); 
    f->occupe = decale(f->occupe, f->te);
    return element;
}

static void *put_fifo_no_shift(fifo *f, void *pelem){
    if(f->libre == f->last){
        return NULL;
    }
    f->libre = pelem;
    f->libre = decale(f->libre, f->te);
    
}

int main(){
    puts("main");
    return EXIT_SUCCESS;
}
