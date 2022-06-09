#include "lists.h"
#include <stdio.h>
/**
* insert_node - Inserts a node in a sorted linked list
* @head: Pointer to a pointer pointing to the head node in a linked list
* @number: Number to be inserted.
*
* Return: Pointer to the new node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}

	new->next = node->next;
	node->next = new;
	return (new);
}
