import math
import random
import sys
import string

nom_fic = sys.argv[1]
coef = int(sys.argv[2])
liste=[]


f = open(nom_fic, 'r')
#lire la ligne vide
numbers=f.readline()
#lire la premiere ligne
numbers=f.readline()

n=0
k=0

com=1
while(numbers!=""):
    #print '%s' % numbers
    numbers = numbers.split(",")
    numbers.pop()
    numbers = list(map(int, numbers))
    if(len(numbers)>k and com<499 and k>=0 and n>0):
        print '%d,' % (numbers[k])
        com=com+1
    numbers=f.readline()
    n=n+1
    if(n>1):
        k=n
    else:
        k=1
