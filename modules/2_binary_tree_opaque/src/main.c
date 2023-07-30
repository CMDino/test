#include <stdio.h>
#include <stdlib.h>

#include "binary_tree.h"

int main(void)
{
  binary_tree_t* bt = bt_create();
  bt_print(bt, bt_print_in);
  bt_insert(bt, (void*) 0, 2);
  bt_insert(bt, (void*) 1, 0);
  bt_insert(bt, (void*) 2, 3);
  bt_insert(bt, (void*) 3, -2);
  bt_insert(bt, (void*) 4, 13);
  bt_insert(bt, (void*) 5, 10);
  bt_insert(bt, (void*) 6, -7);
  bt_print(bt, bt_print_in);
  bt_print(bt, bt_print_pre);
  bt_print(bt, bt_print_post);
  bt_free(&bt);

  return 0;
}