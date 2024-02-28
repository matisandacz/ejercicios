#include <stdio.h>
#include <stdbool.h>

/*
 * Determina si un número es par
 */
bool es_par(int numero){
    return numero % 2 == 0;
}

/*
 * Determina si un año es bisiesto
 * Un año es bisiesto si es disible entre 4, pero si es divisible entre 100 solo puede ser bisiesto si tambien lo es por 400.
 */
bool es_bisiesto(int anio){
    return anio % 400 == 0 || (anio % 4 == 0 && !(anio % 100 == 0));
}

int main(){
    // Test 1
    if(es_par(1)){
        printf("Error es_par para número 1.\n");
    } else {
        printf("Test es_par número 2 correcto.\n");
    }

    // Test 2
    if(!es_par(2)){
        printf("Error es_par para número 2.\n");
    } else {
        printf("Test es_par número 2 correcto.\n");
    }

    // Test 3
    if(!es_par(0)){
        printf("Error es_par para número 0.\n");
    } else {
        printf("Test es_par número 0 correcto.\n");
    }

    // Test 4
    if(!es_bisiesto(2008)){
        printf("Error es_bisiesto para 2008.\n");
    } else {
        printf("Test es_bisiesto para 2008 correcto.\n");
    }

    // Test 4
    if(es_bisiesto(2007)){
        printf("Error es_bisiesto para 2007.\n");
    } else {
        printf("Test es_bisiesto para 2007 correcto.\n");
    }

    // Test 5
    if(es_bisiesto(2100)){
        printf("Error es_bisiesto para 2100.\n");
    } else {
        printf("Test es_bisiesto para 2100 correcto.\n");
    }

    // Test 6
    if(!es_bisiesto(400)){
        printf("Error es_bisiesto para 400.\n");
    } else {
        printf("Test es_bisiesto para 400 correcto.\n");
    }
}