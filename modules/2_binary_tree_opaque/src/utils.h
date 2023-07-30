#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>

void struct_print_msg(char* struct_name, char* struct_function, char* msg)
{
  printf("MSG(%s, %s): %s", struct_name, struct_function, msg);
}
void struct_print_err(char* struct_name, char* struct_function, char* msg)
{
  printf("ERR(%s, %s): %s", struct_name, struct_function, msg);
}

#endif // UTILS_H