#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - This func checks if a singly linked list
 * has a cycle in it
 * @list: The list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cheetah = list, *snail = list;
	int found = 0;

	while ((cheetah && snail) && snail->next)
	{
		snail = snail->next;

		if (cheetah->next || cheetah->next->next)
			cheetah = cheetah->next->next;
		else
		{
			break;
		}
		if (snail == cheetah)
		{
			found = 1;
			break;
		}
	}
	return (found);
}
