#ifndef MY_HEADER_H
#define MY_HEADER_H

/**
 * struct dlistint_s - doubly linked list
 * @n: integer
 * @prev: points to the previous node
 * @next: points to the next node
 *
 * Description: doubly linked list node structure
 */
typedef struct dlistint_s
{
	int n;
	struct dlistint_s *prev;
	struct dlistint_s *next;
} dlistint_t;

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#endif
