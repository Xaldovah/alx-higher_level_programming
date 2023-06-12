#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head - ...
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	if (*head == NULL)
		return 1;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = reverse(slow);
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return 0;
		slow = slow->next;
		fast = fast->next;
	}
	return 1;
}

/**
 * reverse - ...
 * @head: ...
 *
 * Return: ...
 */

listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL, *curr = head, *next;
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}
