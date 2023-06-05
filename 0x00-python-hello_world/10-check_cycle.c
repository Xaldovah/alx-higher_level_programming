#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: The list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *cheetah = list;
	listint_t *snail = list;

	while (cheetah && snail && snail->next)
	{
		snail = snail->next;
		cheetah = cheetah->next->next;

		if (snail == cheetah)
			return 1;
	}
	return 0;
}
