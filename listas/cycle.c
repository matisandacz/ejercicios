#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct ListNode {
	int val;
	struct ListNode* next;
} ListNode;


/*

Dada una lista enlazada, determinar si tiene un ciclo.

*/
bool hasCycle(ListNode* node)
{

	if(!node)
	{
		return false;
	}

	ListNode* slow = node;
	ListNode* fast = node->next;

	while(slow != fast)
	{

		if(!fast || !(fast->next))
		{
			return false;
		}

		slow = slow->next;
		fast = fast->next->next;
	}

	return true;
}

int main(){
	// Esto es un comentario

	ListNode* node1 = (ListNode*) malloc(sizeof(ListNode));
	ListNode* node2 = (ListNode*) malloc(sizeof(ListNode));
	ListNode* node3 = (ListNode*) malloc(sizeof(ListNode));

	node1->next = node2;
	node2->next = node3;
	node3->next = NULL;

	printf("List 1 -> 2 -> 3 has cycle: %s\n", hasCycle(node1)?"true":"false");

	node3->next = node2;

	printf("List 1 -> 2 -> 3 -> 2 has cycle: %s\n", hasCycle(node1)?"true":"false");

	free(node1);
	free(node2);
	free(node3);

}