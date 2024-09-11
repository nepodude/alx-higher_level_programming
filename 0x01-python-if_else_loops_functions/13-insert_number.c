#include "lists.h"

/**
* insert_node - inserts one node.
* @head: head of the node.
* @number: number to insert in the node.
* Return: the address of the inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return(new_node);
	}
	current = *head;
	while(current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;

	return new_node;
}