#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function succeeds - a pointer to the new node.
 *         Otherwise - NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	node = *head;

	while (node->next != NULL && node->next->n < number)
	{
		node = node->next;
	}

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
