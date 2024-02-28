#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Persona{
	char* nombre;
	int edad;
} Persona;

void masGrande(Persona** personas, int n){
	// TODO
}

int main(){
	
	Persona** personas = (Persona**) malloc(sizeof(Persona*) * 2);

	for(int i = 0 ; i < 2 ; i++){
		personas[i] = (Persona*) malloc(sizeof(Persona));
	}

	personas[0]->edad = 23;
	personas[0]->nombre = (char*) malloc(2);
	personas[0]->nombre[0] = 'M';


	personas[1]->edad = 22;
	personas[1]->nombre = (char*) malloc(2);
	personas[1]->nombre[0] = 'T';

	masGrande(personas, 2);

}


