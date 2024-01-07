#include"lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    static listint_t *temp;

    if (current == NULL)
        return (1);

    if (temp == NULL)
        temp = current;

    if (is_palindrome(&current->next) && temp->n == current->n)
    {
        temp = temp->next;
        return (1);
    }
    else
        return (0);
}
