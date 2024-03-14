#include <stdlib.h>
#include <stdio.h>

typedef struct Nodo {
	int val; 
	struct node_t* sig;
} node_t;

void imprimirValores(node_t* node_t) {
	while(node_t){
		printf("El valor del node_t es: %d\n", node_t->val);
		node_t = node_t->sig;
	}
}

int main(){
	
	node_t* node1 = (node_t*) malloc(sizeof(node_t));
	node_t* node2 = (node_t*) malloc(sizeof(node_t));
	node_t* node3 = (node_t*) malloc(sizeof(node_t));

	node1->sig = node2;
	node1->val = 1;

	node2->sig = node3;
	node2->val = 2;

	node3->sig = NULL;
	node3->val = 3;

	imprimirValores(node1);

	free(node1);
	free(node2);
	free(node3);

}



