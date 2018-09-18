#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - function that checks is a linked list is a palindrome
 * @head: double pointer to a linked list
 * Return: 1 if linked list is a palindrome, or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int str[2000];
	int i, j;

	if (!head || !(*head) || !((*head)->next))
		return (1);
	temp = *head;
	i = 0;
	while (temp)
	{
		str[i] = temp->n;
		i++;
		temp = temp->next;
	}
	i--;
	for (j = 0; j <= i / 2 + 1; j++, i--)
	{
		if (str[i] == str[j])
			continue;
		else
			return (0);
	}
	return (1);
}
