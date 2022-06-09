#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: linked list to check
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *fast_point = list;
	listint_t *slow_point = list;

	if (list == NULL)
		return (0);

	while (fast_point != NULL && slow_point != NULL && fast_point->next)
	{
		slow_point = slow_point->next;
		fast_point = fast_point->next->next;
	if (fast_point == slow_point)
		return (1);
	}

	return (0);
}
