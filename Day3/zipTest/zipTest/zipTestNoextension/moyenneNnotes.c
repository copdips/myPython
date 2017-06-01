#include <stdio.h>

int main(void)
{
    int nbNotes, note ;
    printf("combien de note y a-t-il ? ");
    scanf("%d",&nbNotes);
    int somme = 0;
    for (int i = 0; i < nbNotes; ++i){
        printf("entrer la note numéro numero %2d :   ",i+1);
        scanf("%d", &note);
        somme = somme + note ;
    }
    printf("moyenne des notes : %5.2f \n", ((double)somme)/nbNotes);
    return 0;
}
