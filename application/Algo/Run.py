import sys
import os
sys.path.append(os.path.dirname(__file__))
import mylib
import random

def run():

    solution=mylib.my_fonction(random.randrange(0,10),random.randrange(0,10))

    N=100
    tab=mylib.intArray(N)
    for i in range(N):
        tab[i]=random.randrange(0,10)
    solution_tab=mylib.my_fonction_tab(tab,N)
    return [solution,solution_tab]
