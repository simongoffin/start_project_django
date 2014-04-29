#include "fonction.h"

int my_fonction(int x,int y)
{
    int solution(x+y);
    return solution;
}

int my_fonction_tab(int *tab,int taille)
{
    int somme(0);
    for(int i(0);i<taille;i++)
    {
        somme=somme+tab[i];
    }
    return somme;
}
