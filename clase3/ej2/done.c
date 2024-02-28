#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Persona{
	char* nombre;
	int edad;
} Persona;

void masGrande(const Persona** personas, int n){

	Persona* mayor = personas[0];

	for(int i = 1; i < n; i++){
		Persona* persona = personas[i];
		if(persona->edad > mayor->edad){
			mayor = persona;
		}
	}
	printf("%s es la persona mas grande, de edad %d\n", mayor->nombre, mayor->edad);
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


