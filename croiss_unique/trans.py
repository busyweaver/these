import cfu
import sys
import string
import prm

def permtoarb(p,res):
    if(len(p)==1):
        return res
    if(len(p)==2):
        #normalement cest forcement 2,1 au debut
        return res.append([1,2])
        

    orig=origtaille(p)
   # print orig
    comp_orig=orig+1
   # print comp_orig
   # print [indice(comp_orig,p),len(p)-orig+1]
    if(orig==1):
        res.append([1,len(p)-orig+1])
    else:
        res.append([indice(comp_orig,p)+1,len(p)-orig+1])



    
    y=supprimer_traite(p,orig)
   # print y
    permtoarb(y,res)
    

def origtaille(p):
    orig=len(p)-1
    pos=len(p)
    while(pos==p[pos-1] and orig>=2):
        pos=pos-1
        orig=orig-1
    return orig


def indice(x,tab):
    #print x
    #print tab
    for i in range(0,len(tab)):
        if(tab[i]==x):
            return i
    print "erreur non indice"
    sys.exit(-1)

def supprimer_traite(p,x):
    np = []
    for i in range(0,len(p)):
        if(p[i]<=x):
            np.append(p[i])
    return np


def arbtoperm(arbre,res):
    arb=arbre[:]
    x = arb[len(arb)-1]
    for i in range(1,x[1]+1):
        res.append(i)
    
    del arb[len(arb)-1]
    
    while(len(arb)!=0):
        x = arb[len(arb)-1]
        if(x[1]>2):
            #ajouter a la perm x[1] - 2 elem a la fin
            va = x[1]-2
            garde = len(res)+1
          #  print res
            while(va>0):
                res.insert(len(res),len(res)+2)
                va=va-1
          #  print res
            res.insert(x[0]-1,garde)
        else:
            res.insert(x[0]-1,len(res)+1)
        del arb[len(arb)-1]


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


################### DESSIN ARBRE #########################

def gene_dot(noeuds):
    fil = open("essai.gv",'w')
    fil.write("digraph G {\n")
    ecrit(fil,noeuds)
    

    fil.write("}\n")

def ecrit(fil,noeuds):
 
    if not(noeuds[2]==None):
        fil.write(string.join([str(noeuds[0]),"[shape=plaintext,label=\"",str(noeuds[1]),"\"]","\n"], " "))
        i = len(noeuds)
        for z in noeuds[2]:
            #a rajouter label voir format
            fil.write(string.join([str(noeuds[0]),"->",str(z[0]),"\n"]," "))
            ecrit(fil,z)

        fil.write("\n")
    else:
        fil.write(string.join([str(noeuds[0]),"[shape=plaintext, label=\" - \"]","\n"], " "))
            
   

##############" BIJECTION INTERMEDIAIRE ##################

def recon_arbre(noeuds):
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
                
