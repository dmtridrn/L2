#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>
#include"afficheur.c"


node *cons_tree(int val, node *tl, node *tr){
    node *tree =malloc(sizeof(node));
    assert(tree != NULL);
    tree->val = val;
    tree->left = tl;
    tree->right = tr;
    return tree;
}

void free_tree(node *t){
    if(t == NULL) {
        return;
    }
    free_tree(t->left);
    free_tree(t->right);
    free(t);
}

int size_tree(node *t){
    if(t == NULL){
        return 0;
    }
    return(1+size_tree(t->left) + size_tree(t->right));
}

int sum_tree(node *t){
    if(t == NULL){
        return 0;
    }
    return(t->val + sum_tree(t->left) + sum_tree(t->right));
}

int depth_tree(node *t){
    if(t == NULL){
        return 0;
    }
    int maxr = 1 + depth_tree(t->right);
    int maxl = 1 + depth_tree(t->left);
    int max = 0;
    if(maxr > maxl){
        max = maxr;
    }
    else{
        max = maxl;
    }
    return max;
}

void print_abr(node *t){
    if(t == NULL){
        return;
    }
    print_abr(t->left);
    printf("%i ", t->val);
    print_abr(t->right);

}

node *insert_abr(node *t, int val){
    if(t == NULL){
        return cons_tree(val, NULL, NULL);
    }
    if(val < t->val){
        t->left = insert_abr(t->left, val);
    }
    else{
        t->right = insert_abr(t->right, val);
    }
    return t;
}

node *search_abr(node *t, int val){
    if(t == NULL){
        return NULL;
    }
    if(t->val == val){
        return t;
    }
    if(t->val > val){
        return search_abr(t->left, val);
    }
    else{
        return search_abr(t->right, val);
    }
}

node *max_abr(node *t){
    if(t == NULL){
        return NULL;
    }
    if(t->right == NULL){
        return t;
    }
    return max_abr(t->right);
}

node *min_abr(node *t){
    if(t == NULL){
        return NULL;
    }
    if(t->left == NULL){
        return t;
    }
    return min_abr(t->left);
}

int check_abr(node *t){
    if(t == NULL){
        return NULL;
    }
    int max = max_abr(t);
    int min = min_abr(t);
    if(t->val < max && t->val > min){
        
    }
}



















int main(){
    node *t = NULL;
    int vals[10] = {8, 3, 1, 2, 6, 4, 7, 10, 14, 13};
    
    printf("=== Building tree ===\n");
    for (int i = 0; i < 10; i++) {
        t = insert_abr(t, vals[i]);
        printf("Inserted %d\n", vals[i]);
    }
    
    printf("\n=== Tree visualization ===\n");
    pretty_print(t);
    
    printf("\n=== Tree properties ===\n");
    printf("Size: %d nodes\n", size_tree(t));
    printf("Sum: %d\n", sum_tree(t));
    printf("Depth: %d\n", depth_tree(t));
    
    printf("\n=== In-order traversal ===\n");
    print_abr(t);
    printf("\n");
    
    printf("\n=== Search tests ===\n");
    int search_vals[] = {6, 4, 15, 0};
    for (int i = 0; i < 4; i++) {
        node *found = search_abr(t, search_vals[i]);
        if (found != NULL) {
            printf("Value %d found!\n", search_vals[i]);
        } else {
            printf("Value %d not found.\n", search_vals[i]);
        }
    }
    
    printf("\n=== Min/Max tests ===\n");
    node *min_node = min_abr(t);
    node *max_node = max_abr(t);
    if (min_node != NULL) {
        printf("Minimum value: %d\n", min_node->val);
    }
    if (max_node != NULL) {
        printf("Maximum value: %d\n", max_node->val);
    }
    
    printf("\n=== Subtree Min/Max tests ===\n");
    node *subtree = search_abr(t, 6);
    if (subtree != NULL) {
        printf("Subtree at node 6:\n");
        min_node = min_abr(subtree);
        max_node = max_abr(subtree);
        if (min_node != NULL) {
            printf("Minimum value in subtree: %d\n", min_node->val);
        }
        if (max_node != NULL) {
            printf("Maximum value in subtree: %d\n", max_node->val);
        }
    }
    
    printf("\n=== Cleaning up ===\n");
    free_tree(t);
    printf("Tree freed successfully!\n");
    
    return 0;
}