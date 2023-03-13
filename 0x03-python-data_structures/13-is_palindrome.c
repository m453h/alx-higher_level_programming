#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to the listint_t head.
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nxt_node, *prev_node;

	if (head == NULL || *head == NULL)
		return (NULL);

	prev_node = NULL;

	while ((*head)->next != NULL)
	{
		nxt_node = (*head)->next;
		(*head)->next = prev_node;
		prev_node = *head;
		*head = nxt_node;
	}

	(*head)->next = prev_node;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the linked list.
 *
 * Return: (int) (1) - If the linked list is a palindrome ELSE (0)
 */
int is_palindrome(listint_t **head)
{
	listint_t *a = *head;
	listint_t *b = *head;

	if (*head == NULL)
		return (1);

	while (b != NULL && b->next != NULL && b->next->next != NULL)
	{
		a = a->next;
		b = b->next->next;
	}

	a = reverse_listint(&a);
	b = *head;
	while (a != NULL && b != NULL)
	{
		if (a->n != b->n)
			return (0);
		a = a->next;
		b = b->next;
	}

	return (1);
}
