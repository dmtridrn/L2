#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>

typedef struct node {
    int val;
    struct node *prev;
    struct node *next;
} node;

typedef struct{
    node *first;
    node *last;
} dl_list;


void print_dl(dl_list *list){
    node *curr = list->first;
    while(curr->next != NULL){
        printf("%i ", curr->val);
        curr = curr->next;
    }
    printf("%i\n", curr->val);
}

void print_dl_rev(dl_list *list){
    node *curr = list->last;
    while(curr->prev != NULL){
        printf("%i ", curr->val);
        curr = curr->prev;
    }
    printf("%i\n", curr->val);
}

dl_list *dl_alloc(){
    dl_list *liste = malloc(sizeof(dl_list));
    assert(liste != NULL);
    liste->first = NULL;
    liste->last = NULL;
    return liste;
}

void dl_free(dl_list *list){
    node *curr = list->first;
    while (curr != NULL) {
        node *next = curr->next;
        free(curr);
        curr = next;
    }
    free(list);
}

node *elmt_alloc(int val){
    node *elmt = malloc(sizeof(node));
    assert(elmt != NULL);
    elmt->val = val;
    elmt->next = NULL;
    elmt->prev = NULL;
    return elmt;
}

void elmt_free(node *elmt){
    if(elmt == NULL){
        return;
    }
    free(elmt);
}

void link_nodes(dl_list *list, node *elmt_l, node *elmt_r){
    if(elmt_l == NULL){
        list->first = elmt_r;
        return;
    }
    else if(elmt_l == NULL){
        list->last = elmt_l;
        return;
    }
    else{
        elmt_l->next = elmt_r;
        elmt_r->prev = elmt_l;
    }
}

node *after(dl_list* list, node* elmt, int val){
    if(elmt == NULL){
        return list->first;
    }
    return elmt->next;
}

void insert_after(dl_list* list, node* elmt, int val){
    node* mario = elmt_alloc(val);
    if(list->first == NULL) {
        list->first = mario;
        list->last = mario;
        return;
    }
    if(elmt == NULL){
        mario->next = list->first;
        list->first->prev = mario;
        list->first = mario;
    }
    else{
        mario->prev = elmt;
        mario->next = elmt->next;
        if(elmt->next != NULL){
            elmt->next->prev = mario;
        } else {
            list->last = mario;
        }
        elmt->next = mario;
    }
}

node *before(dl_list* list, node* elmt, int val){
    if(elmt == NULL){
        return list->last;
    }
    return elmt->prev;
}

void insert_before(dl_list* list, node* elmt, int val){
    node* mario = elmt_alloc(val);
    if(list->last == NULL) {
        list->last = mario;
        list->first = mario;
        return;
    }
    if(elmt == NULL){
        mario->prev = list->last;
        list->last->next = mario;
        list->last = mario;
    }
    else{
        mario->next = elmt;
        mario->prev = elmt->prev;
        if(elmt->prev != NULL){
            elmt->prev->next = mario;
        } else {
            list->first = mario;
        }
        elmt->prev = mario;
    }
}




int main() {
    node *n1 = malloc(sizeof(node));
    node *n2 = malloc(sizeof(node));
    node *n3 = malloc(sizeof(node));

    n1->val = 1; n1->prev = NULL; n1->next = n2;
    n2->val = 2; n2->prev = n1;   n2->next = n3;
    n3->val = 3; n3->prev = n2;   n3->next = NULL;

    dl_list list;
    list.first = n1;
    list.last = n3;

    printf("Liste dans l'ordre : ");
    print_dl(&list);

    printf("Liste en sens inverse : ");
    print_dl_rev(&list);

    free(n1);
    free(n2);
    free(n3);

    return 0;
}
