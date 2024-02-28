#include <stdio.h>
#include <stdbool.h>

int suma(int n){
	int suma = 0;
	for(int i=1; i<n; i++){
		if(i%2==1){
			suma = suma + i;
		}
	}
	return suma;
}

int main(){
	printf("%d\n", suma(10));
}