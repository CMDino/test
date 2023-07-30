#ifndef BINARY_TREE_C
#define BINARY_TREE_C

#include "binary_tree.h"
#include "utils.h"

#include <stdio.h>
#include <stdlib.h>

typedef struct node_t
{
  void* data;
  int weight;
  struct node_t* left;
  struct node_t* right;
} node_t;

typedef struct binary_tree_t
{
  node_t* root;
  int max_depth;
  int num_nodes;
} binary_tree_t;

////////////////////////////////////////// STATIC FUNCTIONS

static node_t* node_create(void* data, int weight)
{
  node_t* node = (node_t*) malloc(sizeof(node_t));
  node->data = data;
  node->weight = weight;
  node->left = NULL;
  node->right = NULL;

  return node;
}

static void bt_insert_r(node_t** root, void* data, int weight)
{
  if((*root) != NULL)
  {
    if((*root)->weight > weight)
    {
      bt_insert_r(&((*root)->left), data, weight);
    }
    else
    {
      bt_insert_r(&((*root)->right), data, weight);
    }
  }
  else
  {
    (*root) = node_create(data, weight);
  }
}

static void bt_print_r_in(node_t* root)
{
  if(root != NULL)
  {
    bt_print_r_in(root->left);
    printf("%d ", root->weight);
    bt_print_r_in(root->right);
  }
}

static void bt_print_r_pre(node_t* root)
{
  if(root != NULL)
  {
    printf("%d ", root->weight);
    bt_print_r_pre(root->left);
    bt_print_r_pre(root->right);
  }
}

static void bt_print_r_post(node_t* root)
{
  if(root != NULL)
  {
    bt_print_r_post(root->left);
    bt_print_r_post(root->right);
    printf("%d ", root->weight);
  }
}

static void bt_free_r(node_t** root)
{
  if(*root != NULL)
  {
    bt_free_r(&((*root)->left));
    bt_free_r(&((*root)->right));
    free(*root);
    *root = NULL;
  }
}

////////////////////////////////////////// FUNCTIONS

binary_tree_t* bt_create()
{
  binary_tree_t* bt = (binary_tree_t*) malloc(sizeof(binary_tree_t));
  
  bt->root = NULL;
  bt->max_depth = 0;
  bt->num_nodes = 0;

  struct_print_msg("binary_tree_t", "bt_create", "instance created.\n");

  return bt;
}

void bt_insert(binary_tree_t* bt, void* data, int weight)
{
  bt_insert_r(&(bt->root), data, weight);
  struct_print_msg("binary_tree_t", "bt_insert", "new node inserted.\n");
  bt->num_nodes++;  
}

void bt_print(binary_tree_t* bt, bt_print_t mode)
{
  if(bt->root != NULL)
  {
    if(mode == bt_print_in)
    {
      struct_print_msg("binary_tree_t", "bt_print", "printing weights in IN_ORDER mode: ");
      bt_print_r_in(bt->root);
    }
    else if(mode == bt_print_pre)
    {
      struct_print_msg("binary_tree_t", "bt_print", "printing weights in PRE_ORDER mode: ");
      bt_print_r_pre(bt->root);
    }
    else if(mode == bt_print_post)
    {
      struct_print_msg("binary_tree_t", "bt_print", "printing weights in POST_ORDER mode: ");
      bt_print_r_post(bt->root);
    }
    else
    {
      struct_print_err("binary_tree_t", "bt_print", "specified mode is no valid.");
    }
  }
  else
  {
    struct_print_msg("binary_tree_t", "bt_print", "tree is empty.");
  }

  printf("\n");
}

void bt_free(binary_tree_t** bt)
{
  if((*bt) != NULL && (*bt)->root != NULL)
  {
    bt_free_r(&((*bt)->root));
    free(*bt);
    *bt = NULL;
    struct_print_msg("binary_tree_t", "bt_free", "memory released.\n");
  }
}

#endif // BINARY_TREE_C