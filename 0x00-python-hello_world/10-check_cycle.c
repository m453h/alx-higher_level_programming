#include "lists.h"

/**
 *
 * check_cycle - checks if linked list has a cycle in it
 * @list: the pointer to the first node of the linked list
 * Return: (int) - (1) if has cycle ELSE (0)
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow_ptr = list->next;
	fast_ptr = list->next->next;

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	return (0);
}
