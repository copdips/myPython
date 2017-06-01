#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    int entiers[5] ;
    printf("adresse de entiers :  %p \n",entiers);
    printf("adresse de entiers :  %p \n", entiers+1);
    printf("adresse de entiers :  %p \n", entiers+2);
    printf("adresse de entiers :  %p \n", entiers+3);
    printf("adresse de entiers :  %p \n", entiers+4);
    printf("adresse de entiers :  %p \n", entiers+5);

    printf("adresse de entiers :  %d \n", entiers[0]);
    printf("adresse de entiers :  %d \n", entiers[1]);
    printf("adresse de entiers :  %d \n", entiers[2]);
    printf("adresse de entiers :  %d \n", entiers[3]);
    printf("adresse de entiers :  %d \n", entiers[4]);
    printf("adresse de entiers :  %d \n", entiers[5]); // hors tableau


    float *tabdyn;    /* Declaration pointeur */

    /* Allocation pour 1000 reels */
    tabdyn = malloc(1000 * sizeof(float));

    /* Utilisation ... idem tableau static */
    tabdyn[0] = 0.5;


    /* Liberation de la zone : ne pas oublier */
    free(tabdyn);

    return 0;
}
