#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *tmp;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	if (!*head)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	current = *head;
	
	while (current->next)
	{
		if (current->next->n >= number)
		{
			tmp = current->next;
			current->next = new;
			new->next = tmp;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	new->next = NULL;
	return new;
}
