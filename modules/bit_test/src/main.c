#ifndef MAIN_C
#define MAIN_C

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main()
{
	uint8_t value = 0b01000100;
	uint8_t result = value << 3;

	printf("Original value: %d\n", value);
	printf("Result: %d\n", result);

	return 0;
}

#endif // MAIN_C
