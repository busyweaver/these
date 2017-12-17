import math
import random
import sys
import string
#noeuds=[]
bino={}
com1=1
som_nk={}
#hello moto

def trouverarbre(n,N,F,to,noeuds):
#    print 'N%d' % N
#    print 'K%d' % K
  #  print 'n===%d' % n
    if N==0:
        print 'erreur'
        return to
    if N==1:
        if n !=1:
            print 'erreur'
        return to
    CO=CON[N]
    re=trouverfk(n,CO)
    ri=trouverfk(int(math.ceil(re[1]/float(kf[re[0]]))),som_nk[(N,re[0])])
    tmp=trouvernoeuds(N,re[0],int(math.ceil(re[1]/float(kf[re[0]]))),ri[0],ri[1],noeuds)
    #print 'tmp = %s' % (str(tmp))
    maj_arbre(tmp,to)

    trouverarbre(int(math.ceil(re[1]/float(CON[N][re[0]]/float(F[re[0]])))),re[0],F,to,noeuds)          

def trouvernoeuds(N,k,ab,i,ab2,noeuds):
    l = composition(N-k,i)
    comp=l[int(math.ceil(ab2/float(binomial(k,i)*pow(2,k-i))))-1]
   # print 'comp choisie %s' % (str(comp))
    #rajouter les noeuds 1
    ra= maj_noeuds(comp,N,k,i)
    const_arbre(N,i,k,comp,noeuds)
    return ra



def maj_noeuds(comp,N,k,i):
    #on construit un tableau selon les arites
    ra=[]
    for z in range(0,N):
        ra.append(0)
   
    for e in comp:
        ra[e]=ra[e]+1
    for df in range(0,k-i):
        lm = random.randint(0,1)
        ra[0]=ra[0]+lm
    return ra

def const_arbre(N,i,k,comp,noeuds):
    nodes=[]
    for bb in range(0,k):
        nodes.append(None)
    #je pense
    nb_feuilles_choisies=i
    dict={}
    qw=0
    while nb_feuilles_choisies>0:
        #code bon mais pas efficace
        q=random.randint(0,k-1)
        if not(q in dict):
            nodes[q]=comp[qw]+1
            dict[q]=0
            qw=qw+1
            nb_feuilles_choisies=nb_feuilles_choisies-1
   
    for jk in range(0,len(nodes)):
        if(nodes[jk]==None):
            fg=random.randint(0,1)
            if(fg==1):
                nodes[jk]=1
   
    noeuds.append(nodes)

def maj_arbre(tmp,res):
    for i in range(0,len(res)):
        if i<len(tmp):
            res[i]=tmp[i]+res[i]



def trouverfk(n,CO):
    ab=n
    m=len(CO)-1
    while (ab>0):
        ab=ab-CO[m]
        m=m-1
    
    m=m+1
    ab=ab+CO[m]
    return [m,ab]
    
    
#Ce code n'est pas a moi(recupere sur un site internet)
def composition(n, length):
#    print 'n= %d' % n
#    print 'length= %d' % length
    
    result = []
    a = [0 for i in range(n + 1)]
    k = 1
    a[0] = 0
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while 1 <= y:
            a[k] = x
            x = 1
            y -= x
            k += 1
        a[k] = x + y
        if not length or len(a[:k + 1]) == length:
            result.append(a[:k + 1])
    return result


  
def binomial(n, k):
    if k>n:
        return 0
    if k<0:
        return 0
    
    if((n,k) in bino):
        return bino[(n,k)]
    else:
        result=int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k)))
        bino[(n,k)]=result
    # result = 1
    # for i in range(1, k+1):
    #     result = result * (n-i+1) / i
    return result

#main


N=int(sys.argv[1])
kf = [0,1]


CON=[
    [0],
    [1]
]
           
def recurrence(N):
    for n in range(2,N+1):
        print 'n!===========%d' % n
        tmp = coeff_sum_interne(n,kf)
        kf.append(long(sum(tmp)))
        CON.append(tmp)

            
def coeff_sum_interne(n,kf):
    co=[0L]
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



def un_arbre(t,noeuds):
    to=[]
    for r in range(0,int(t*(t-1)*0.5)+1):
        to.append(0)
    n=random.randint(1,kf[t])
    trouverarbre(n,t,kf,to,noeuds)
    return to

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
         #   print 'tab %s' % str(noeuds[j])
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


    
if(sys.argv[2]=='0'):
    cal_coeff()
    sauv_coeff()

elif(sys.argv[2]=='1'):
    cal_coeff()
    print 'kf %s' % str(kf)
    moy=recursive_generator(int(sys.argv[1]))
#    print 'res %s' % str(moy[0])
    
else:
    
   if(int(sys.argv[3])>int(sys.argv[1])):
       print 'taille arbre demande plus grande que possible'
   else:
       print 'good'
       cal_coeff()
       print 'Co %s' % str(CON[5])
       coq=un_arbre(int(sys.argv[3]))
       # for e in coq:
       #     print '\n'
       #     for i in e :
       #         if not(i==None):
       #             print '%d,' % i
       #         else:
       #             print '*,'
       print 'coq %s' % str(coq)
       noeuds2=recon_arbre(coq)
       taille=height(noeuds2)
       print 'taille %d' % taille
       print 'arbre %s' % str(noeuds2)
       gene_dot(noeuds2)

