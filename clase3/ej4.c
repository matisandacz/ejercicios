#include <stdlib.h>
#include <stdio.h>

typedef struct Persona {
	char* nombre;
	char* apellido;
	int edad;
	long dni;
} person_t;

void imprimirEdad(person_t* person_t){
	printf("La edad es: %d\n", person_t->edad);
}

int main(){

	// Structs con memoria estatica

	person_t mi_person_t;
	mi_person_t.nombre = "Matias";
	mi_person_t.apellido = "Edad";
	mi_person_t.edad = 25;
	mi_person_t.dni = 123456789;
	printf("El nombre es: %s\n", mi_person_t.nombre);

	// Structs con memoria dinamica

	person_t* mi_person_t_2 = (person_t*) malloc(sizeof(person_t));
	mi_person_t_2->nombre = "Matias";
	mi_person_t_2->apellido = "Edad";
	mi_person_t_2->edad = 25;
	mi_person_t_2->dni = 123456789;
	printf("El DNI es: %ld\n", mi_person_t_2->dni);
	imprimirEdad(mi_person_t_2);

	return 0;
}



