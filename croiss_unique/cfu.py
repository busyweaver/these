import math
import random
import sys
import string


#n numero arbre a trouver
#N taille de l arbre
#F recurrence


def trouverarbre(n,N,F,CON,noeuds):
  #  print 'N%d' % N
  #  print 'n%d' % n
   # print 'debut %s' % str(noeuds)
    if N==0:
        print 'erreur'
        return noeuds
    if N==1:
        if n !=1:
            print 'erreur'
        return noeuds
 #   if n==1:
 #       return noeuds.append([1,N])
    CO=CON[N]
    re=trouverfk(n,CO)
  #  print 're %d %d' % (re[0],re[1])
    
    numfeuille=int(math.ceil(re[1]%float(re[0])))+1
    numarbre=int(math.ceil(re[1]/float(re[0])))
    #N-re[0] correspond a l arite de la feuille construite
    noeuds.append([numfeuille,N-re[0]+1])
  #  print 'numf %d  numarbre %d ' % (numfeuille,numarbre)
    #print 'noeuds %s' % str(noeuds)
    trouverarbre(numarbre,re[0],F,CON,noeuds)



def trouverfk(n,CO):
  #  print '%s' % str(CO)
  #  print 'n %d' % n
    ab=n
    m=len(CO)-1
    while (ab>0):
        ab=ab-CO[m]
        m=m-1
    
    m=m+1
    ab=ab+CO[m]
    return [m,ab]
    

#main

           
def recurrence(N,kf,CON):
    for n in range(2,N+1):
        print 'n!===========%d' % n
        tmp = coeff_sum_interne(n,kf)
        kf.append(long(sum(tmp)))
        CON.append(tmp)

            
def coeff_sum_interne(n,kf):
    co=[]
    for i in range(0,len(kf)):
        co.append(i*kf[i])
    return co


def recursive_generator(N):


    elem=[]
    res=[]
    res2=[]
    nb_ok=1
    ind=0
    vb=40
    tabtaille=[]
    for e in [0]:
        print 'nouveau'
        elem.append([])
        res.append([])
        res2.append([])
        for r in range(0,int(N*(N-1)*0.5)+1):
            elem[ind].append(0)
            res[ind].append(0)
            res2[ind].append(0)
            #calcul origine de l arbre
      
        taille=0
        noeuds=[]
        while nb_ok<=10000:
            if(nb_ok % 100==0):
                print '%d' % nb_ok
            to=un_arbre(vb,elem[ind])
           # print 'recur %s' % str(noeuds)
           # noeuds2=recon_arbre(noeuds)
            ajout_res(res[ind],to)
            nb_ok=nb_ok+1
            for z in range(0,len(elem[ind])):
                elem[ind][z]=0
                #    n=n+1
           # taille=taille + height(noeuds2)
            noeuds=[]
            noeuds2=[]
        print 'res %s ' % (str(res[ind]))
        for z in range(0,len(res[ind])):
            res2[ind][z]=res[ind][z]/float(nb_ok)
        
                
        # prob=0
        # for cv in range(2,len(res[0])):
        #     prob=prob+res[0][cv]
        # print 'proba avant %d' % prob
        # print 'prob %f' % (prob/float(nb_ok))
        tabtaille.append(taille/float(nb_ok))
        nb_ok=1
        
        #ind=ind+1
        vb=vb-5
        print 'fini'
    for yu in range(0,21):
        print '%d %f' % (yu+1,res2[ind][yu])
   # for fg in range(0,len(tabtaille)):
    #    print '%d %f' % (((9-fg+1)*5),tabtaille[fg])
    return res2

def ajout_res(res,elem):
    for z in range(0,len(res)):
        res[z]=res[z]+elem[z]




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
            
   
                


def recon_arbre(noeuds):

    id=[2]
    abr=initialistation(noeuds[len(noeuds)-1],id)
    rac=[1,1,abr]

    for fg in range(1,len(noeuds)):
 
        j=len(noeuds)-1-fg
        decalage=0
        for k in range(0,len(noeuds[j])):
        #    print 'boucle %d' % k
            print 'tab %s' % str(noeuds[j])
         #   print 'decalage %d' % decalage
            if not(noeuds[j][k]==None):
                etendre(decalage+k,noeuds[j][k],rac,fg+1,id)
                decalage=decalage+noeuds[j][k]-1
  #  print 'cloche %s' % str(rac)
    return rac
            


def etendre(k,ari,rac,lab,id):
   # print 'label %d' % lab
   # print 'arite %d' % ari
    x=trouver_feuille(k,rac)
    etendre_feuille(x,ari,lab,id)


def etendre_feuille(x,ari,lab,id):
    #print 'etendre label %d ' % lab
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
    for i in range(0,x[0]):
        a.append([id[0],0,None])
        incr(id)
    return a

        
def trouver_feuille(n,noeuds):
    return trouver_recur(n,noeuds,[0])

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
                
  

def sauv_coeff():
    
    f = open(string.join([sys.argv[1],sys.argv[3]],'_'), 'w')
    for i in range(0,N):
        f.write('\n')
        for j in range(0,int(i*(i-1)*0.5)+1):
           f.write(str(kf[i][j]))
           f.write(',')
    f.close()


def height(arbre):
    maxi=[]
    if(arbre[2]==None):
        return 0
    for df in arbre[2]:
        maxi.append(height(df))
    return 1+max(maxi)






def un_arbre(t,kf,CON):
    #print '%d' % kf[t]
    n=random.randint(1,kf[t]+1)
    print 'numero tire %d sur un total de %d' % (n,kf[t])
    res=[]
    trouverarbre(n,t,kf,CON,res)
    
    return res 
    

def iterateur(t,kf,CON):
    tmp=[]
    res=[]
    for n in range(1,kf[t]+1):
       trouverarbre(n,t,kf,CON,tmp)
      # print '%s' % str(tmp)
       res.append(tmp)
       tmp=[]
    return res

