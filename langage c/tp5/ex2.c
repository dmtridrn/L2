#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>

struct array{
    int *content;
    size_t capacity;
    size_t size;
};
typedef struct array array;

array *array_init(size_t capacity){
    array *arr = malloc(sizeof(array));
    if(arr == NULL){
        return NULL;
    }
    arr -> content = malloc(capacity * sizeof(int));
    if(arr -> content == NULL){
        free(arr);
        return NULL;
    }
    arr -> capacity = capacity;
    arr -> size = 0;
    return arr;
}

void array_destroy(array *pa){
    free(pa->content);
    free(pa);
}

int array_get(array *pa, size_t index){
    assert(index < pa -> size);
    return pa -> content[index];
}

void array_set(array *pa, size_t index, int value){
    assert(index < pa -> size);
    pa -> content[index] = value;
}

bool array_append(array *pa, int value){
    if(pa -> size < pa -> capacity){
        pa -> content[pa -> size] = value;
        pa -> size++;
        return true;
    }
    else{
        return false;
    }
}

void array_print(array *pa) {
    printf("Contenu du array: [");
    for (int i = 0; i < pa->size; i++) {
        printf("%i", pa->content[i]);
        if (i < pa->size - 1) {
            printf(" ");
        }
    }
    printf("]\n");
}

int *array_search(array *pa, int value){
    for(int i = 0; i<pa->size; i++){
        if(pa->content[i] == value){
            int *adr = pa -> content + i;
            return adr;
        }
    }
    return NULL;
}

array *array_init_from(int *data, size_t length, size_t capacity){
    assert(capacity >= length);
    array *arr = array_init(capacity);
    for(size_t i = 0; i < length; i++){
        arr -> content[i] = data[i];
        arr->size++;
    }
    return arr;
}

void array_remove(array *pa, size_t index){
    assert(index < pa->size);
    for(size_t i = index; i<pa->size-1; i++){
        pa -> content[i] = pa->content[i+1];
    }
    pa->size--;
}

void array_insert(array *pa, size_t index, int value){
    assert(index < pa->size);
    if(pa->size == pa->capacity){
        pa->content = realloc(pa, 2*(pa->capacity)*sizeof(int));
    }
    if(pa->size <= pa->capacity){
        if(index == pa->size){
            pa->content[index] = value;
            pa->size++;
        }
        else{
            for(size_t i = pa->size; i>index; i--){
                pa->content[i] = pa->content[i-1];
            }
            pa->content[index] = value;
            pa->size++;
        }
    }
}


