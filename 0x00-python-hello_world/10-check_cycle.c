#include "lists.h"
/**
 * check_cycle - function to check if linked list has a cycle in it
 * @list: pointer to linked list
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);
	slow = list;
	fast = slow->next;
	while (fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
