#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ejercicio(char* buffer, size_t len){

	printf("El input fue: %s", buffer);
}

int main(){

	char* buffer = NULL;
	size_t len;

	int read = getline(&buffer, &len, stdin);

	if(read != -1){
		ejercicio(buffer, len);
	} else {
		printf("No se pudo leer nada!\n");
	}

	free(buffer);
	return 0;
}


