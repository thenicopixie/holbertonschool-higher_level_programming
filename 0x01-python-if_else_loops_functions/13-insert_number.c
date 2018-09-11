#include "lists.h"
/**
 * insert_node - function to create new node and insert into linked list
 * @head: double pointer to head of linked list
 * @number: value of node to create
 * Return: address of new node or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!(*head))
		return (NULL);
	if (!head)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	temp = *head;
	while (temp)
	{
		if ((number >= temp->n) && (number <= temp->next->n))
		{
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	return (NULL);
}
