#ifndef BINARY_TREE_H
#define BINARY_TREE_H

typedef struct node_t node_t;
typedef struct binary_tree_t binary_tree_t;
typedef enum bt_print_t { bt_print_in, bt_print_pre, bt_print_post } bt_print_t;

binary_tree_t* bt_create();
void bt_insert(binary_tree_t* bt, void* data, int weight);
void bt_print(binary_tree_t* bt, bt_print_t mode);
void bt_free(binary_tree_t** bt);

#endif // BINARY_TREE_H