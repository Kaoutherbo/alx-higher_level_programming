#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *fast;
    listint_t *slow;

    slow = list;
    fast = list;

    while (slow && fast && fast->next)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}
