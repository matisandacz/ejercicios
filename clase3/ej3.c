#include <stdlib.h>
#include <stdio.h>

struct Persona {
	char* nombre;
	char* apellido;
	int edad;
	long dni;
};

void imprimirEdad(struct Persona* persona){
	printf("La edad es: %d\n", persona->edad);
}

int main(){

	// Structs con memoria estatica

	struct Persona mi_persona;
	mi_persona.nombre = "Matias";
	mi_persona.apellido = "Edad";
	mi_persona.edad = 25;
	mi_persona.dni = 123456789;
	printf("El nombre es: %s\n", mi_persona.nombre);

	// Structs con memoria dinamica

	struct Persona* mi_persona_2 = (struct Persona*) malloc(sizeof(struct Persona));
	mi_persona_2->nombre = "Matias";
	mi_persona_2->apellido = "Edad";
	mi_persona_2->edad = 25;
	mi_persona_2->dni = 123456789;
	printf("El DNI es: %ld\n", mi_persona_2->dni);
	imprimirEdad(mi_persona_2);

	return 0;
}



