#include <stdlib.h>
#include <stdio.h>

typedef struct Nodo {
	int val; 
	struct Nodo* next;
} node_t;

typedef struct Lista {
	node_t* head; 
	int size;
} list_t;


void remove_node(list_t *list, node_t *node) {
	if(node == list->head) {
		list->head = node->next;
		free(node);
		list->size -= 1;
		return;
	}

	node_t* curr = list->head;
	while(curr->next != node){
		curr = curr->next;
	}

	curr->next = curr->next->next;
	free(node);
	list->size -= 1;
	return;
}

int main() {
	return 0;
}