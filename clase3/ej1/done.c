#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void ejercicio(char* buffer, size_t len){

	int cant_palabras = 0;
	for(int i=0; i<len; i++){
		if(buffer[i] == ' '){
			cant_palabras++;
			printf("\n");
		}else{
			printf("%c", buffer[i]);
		}
	}

	printf("Detectamos %d palabras!\n", cant_palabras + 1);
}

int main(){
	char *buffer = NULL;

	size_t len;
	int read = getline(&buffer, &len, stdin);
	if(read != -1){
		ejercicio(buffer, len);
	} else {
		printf("No se leyo ninguna linea\n");
	}

	free(buffer);
	return 0;
}


