import sys
import string
import random
import math

def loigeo(alpha):
    x=random.uniform(0,1)
    res=1
    while(x>0):
        x=x-math.pow(alpha,res)
        res=res+1
    res=res-1
    return res


def un_arbre(iter,alpha,res):
    if iter==0:
        return
     #   return []
    else:
        #print res
        y=loigeo(alpha)
        #print y
        if(len(res)==0):
            res.append([1,y])
         #   res = un_arbre(iter-1,alpha)
         #   return res.append([1,y])
        else:
            x=random.randint(1,sum(e[1] for e in res)-(len(res)-1))
            res.append([x,y])
            #res = un_arbre(iter-1,alpha)
            #return res.append([x,y])
        un_arbre(iter-1,alpha,res)



################## OPERATION #########################

def hauteur(arbre):
    maxi=[]
    if(arbre[2]==None):
        return 0
    for df in arbre[2]:
        maxi.append(hauteur(df))
    return 1+max(maxi)

def nombre_noeuds(arbre):
    #print arbre
    res=[]
    nb=0
    if(arbre[2]==None):
        return 0
    for df in arbre[2]:
        res.append(nombre_noeuds(df))
    return sum(res)+1





##############" BIJECTION INTERMEDIAIRE ##################

def recon_arbre(noeuds):
    noeuds.reverse()
    #print noeuds
    id=[2]
    abr=initialistation(noeuds[len(noeuds)-1],id)
    rac=[1,1,abr]

    for fg in range(1,len(noeuds)):
 
        j=len(noeuds)-1-fg
        decalage=0
        #    print 'boucle %d' % k
         #   print 'tab %s' % str(noeuds[j])
         #   print 'decalage %d' % decalage
        etendre(decalage+noeuds[j][0],noeuds[j][1],rac,fg+1,id)
        decalage=decalage+noeuds[j][0]-1
  #  print 'cloche %s' % str(rac)
    return rac
            






def etendre(k,ari,rac,lab,id):
    # print 'etendre'
    # print rac
    # print k
    # print id
    # print lab
    # print ari
    x=trouver_feuille(k,rac)
    etendre_feuille(x,ari,lab,id)


def etendre_feuille(x,ari,lab,id):
    # print 'etendre feuille'
    # print x
    # print ari
    # print lab
    # print id
    x[1]=lab
    a=[]
    for i in range(0,ari):
        a.append([id[0],0,None])
        incr(id)
    x[2]=a
    
def incr(id):
    id[0]=id[0]+1
    
def initialistation(x,id):
    a=[]
    for i in range(0,x[1]):
        a.append([id[0],0,None])
        incr(id)
    return a

        
def trouver_feuille(n,noeuds):
    return trouver_recur(n,noeuds,[1])

def trouver_recur(n,noeuds,courant):
    if noeuds[2]==None:
        if courant[0]==n:
            return noeuds
        else:
            courant[0]=courant[0]+1
            return []
    else:
        for z in noeuds[2]:
            x=trouver_recur(n,z,courant)
            if(x!=[]):
                return x
    return []
                
