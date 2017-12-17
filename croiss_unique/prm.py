import math
import random
import sys
import string
import itertools
import sys

x=list(itertools.permutations([1,2,3,4]))

def permutation(n):
    tab=[i for i in range(1,n+1)]
    res=list(itertools.permutations(tab))
    return res

def perm_contr(n,x,y):
    tab = permutation(n)
    res=[]
    for i in range(0,len(tab)):
        if(indice(x,tab[i])<indice(y,tab[i])):
            res.append(tab[i])
    return res



def indice(x,tab):
    for i in range(0,len(tab)):
        if(tab[i]==x):
            return i
    print "erreur non indice"
    sys.exit(-1)

def nb_descente(p):
    res = 0
    for i in range(0,len(p)-1):
        if(p[i]>p[i+1]):
            res=res+1
    return res


def nb_montee(p):
    res = 0
    for i in range(0,len(p)-1):
        if(p[i]<p[i+1]):
            res=res+1
    return res

def profil(p):
    print p
    prof=[0 for j in range(0,len(p)+1)]
    i=len(p)
    while(i>1):
        ind = indice(i, p)
        noeud = nb_suitedec(i,ind,p)
        # print 'noeuds'
        # print noeud
        # print (noeud+1)
        
        i=i-noeud-1
        prof[noeud+2]=prof[noeud+2]+1
            
    return prof

def nb_suitedec(i,ind,p):
    # print 'suitedec'
    # print i
    # print ind
    # print p
    if(ind==0):
        return 0
    res = 0
    while(p[ind]==p[ind-1]+1 and p[ind]>2):
        res=res+1
        ind=ind-1
    
    return res
