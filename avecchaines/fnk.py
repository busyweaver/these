import math
import random
import sys
import string
noeuds=[]
bino={}
compo={}
com1=1


#generer_compo_fixe

def verif_nb_elem(n,l):
   # print 'l %s' % str(l)
   # print 'n %d' % n
    x=n
    i=0
    x=x-l[i]+1 
    i=i+1
    while(x>0 and i<len(l)):
        x=x-(l[i]-l[i-1])+i 
        i=i+1
    if(x>0):
        res= i
    else:
        res=i-1        
    return res
def construire_compo(n,indicek):
   # print '%s' % str(indicek)
#    print 'const compo %s %d' % (str(indicek),n)
    indicek.sort()
    tmp=indicek[0]
    compo=[tmp]
    indicek.pop(0)
   # print '%s' % str(indicek)
    while(indicek!=[]):
        compo.append(indicek[0]-tmp)
        
        tmp=indicek[0]
        #print 'tmp %d' % tmp
        indicek.pop(0)
    compo.append(n-tmp)
    return compo


def random_compo(no,k):
    #add initial conditions

    if k==1:
        return [no]
    if k==no:
        return [1 for i in range(no)]
    n=no
    x=random.randint(1,n-1)
    #print 'x %d ' % x
    l=[x]
    n=n-1
    
    for i in range(0,k-2):
        x=random.randint(1,n-1)
        #print 'x %d ' % x
        decalage=verif_nb_elem(x,l)
        l.append(x+decalage)
        l.sort()
        n=n-1

    return construire_compo(no,l)

cof = open("100_coeff"+".txt", 'r')
denom = open("100_denom"+".txt", 'r')

def coef(r,N,s,K):
    x = binomial(r, K-s)*binomial(N+K-r-s-1,K-s-1)
    return x

def trouverarbre(n,N,K,to,noeuds):
    # print 'N%d' % N
    # print 'K%d' % K
    # print 'n!===%d' % n
    if N==0:
        print 'erreur'
        return []
    if N==1:
        if n !=1:
            print 'erreur'
        return to
   # if (K==1 and N>=2):
   #     to[N-1]=to[N-1]+1
   #     return to


    #CO=CON[N][K]
    print 'getco %d %d' % (N,K)
    CO=getco(N,K)
    print 'fingetco %d %d' % (N,K)
    #CO=calcul_CO(N,kf,K)
    # for i in range(0,len(CO)):
    #     print 'nouv'
    #     for j in range(0,len(CO[i])):
    #         print '%d' % CO[i][j]
    
    re=trouverfk(N,K,n,CO)
    r=re[0]
    m=re[1]
    ab=re[2]
 #   print 'r%d' % r
 #   print 'm%d' % m
    tmp=trouvernoeuds(N,K,int(math.ceil(ab/float(getkf(r,m)))),r,m,noeuds)
    maj_arbre(tmp,to)
  
    trouverarbre(int(math.ceil(ab/float(coef(r,N,m,K)))),r,m,to,noeuds)

def trouvernoeuds(N,K,ab,r,s,noeuds):
    #combien de feuilles on ete chosies  
    #on determine la composition
 
    #l=composition(N+K-r-s,K-s,int(math.ceil(ab/float(binomial(r,K-s))))-1)
#    print 'ab%f' % math.ceil(ab/float(binomial(r,K-s)))
#    print 'comp= %d' % (math.ceil(ab/binomial(r,K-s))-1)
   # comp=l[int(math.ceil(ab/float(binomial(r,K-s))))-1]
 
    comp = random_compo(N+K-r-s,K-s)
    #penser a augmenter de 1 la compo
    #for t in range(0,len(comp)):
    #   comp[t]=comp[t]+1
  
    #trouver les chaines unaires
    #for z in range(0,len(comp)):
    #    print 'comp%d' % comp[z]
    
    ra= maj_noeuds(comp,N,K)
    #print 'ra %s' % str(ra)
    const_arbre(N,K,ab,r,s,comp,noeuds)
    return ra




def const_arbre(N,K,ab,r,s,comp,noeuds):
    nodes=[]
    for i in range(0,r):
        nodes.append(None)
    #je pense
    nb_feuilles_choisies=K-s
    dict={}
    qw=0
    while nb_feuilles_choisies>0:
        q=random.randint(0,r-1)
        if not(q in dict):
            nodes[q]=comp[qw]
            dict[q]=0
            qw=qw+1
            nb_feuilles_choisies=nb_feuilles_choisies-1
    noeuds.append(nodes)
    
            
        
  





def maj_noeuds(comp,N,K):
    #on construit un tableau selon les arites
    ra=[]
 
    for z in range(0,N):
        ra.append(0)
   
    for e in comp:
        ra[e-1]=ra[e-1]+1
    return ra

def maj_arbre(tmp,res):
    for i in range(0,len(res)):
        if i<len(tmp):
            res[i]=tmp[i]+res[i]




#a modifier
def trouverfk(N,K,n,CO):

    ab=n
    r=N-1
    m=len(CO[r])-1
    while (ab>0):
        ab=ab-CO[r][m]
        if m-1<0:
            r=r-1
            m=len(CO[r])-1
        else:
            m=m-1
    
    if m==len(CO[r])-1:
        m=0
        r=r+1
    else:
        m=m+1
    ab=ab+CO[r][m]    
    return [r,m,ab]

def composition(n, length,num):
    # print 'compo n= %d' % n
    # print 'compo length= %d' % length

#    if(length==1):
#        return [[n]]
    #if((n,length) in compo):
    #    return compo[(n,length)]
    
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
            if(len(result)==num+1):
                return result
 #   compo[(n,length)]=result
    return result

def ajout_res(res,elem):
   
    for z in range(0,len(res)):
        res[z]=res[z]+elem[z]

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


# N=int(sys.argv[1])
kf = [[0],[1,0]]


CON=[
    [0],
    [ [[1],[0]]       ]
    

]

def cal_coeff(N,K):
    for n in range(2,N+1):
        print 'n!===========%d' % n
        CON.append([0])
        kf.append([0])
        for k in range(1, int((n)*(n-1)*0.5)+1):
            tmp = calcul_CO(n,kf,k)
            kf[n].append( tmp[0][0])
            tmp[0][0]=0
            CON[n].append(tmp)
         #   if(sys.argv[2]=='1' or sys.argv[2]=='2'):
         
       
def calcul_CO(N,kf,K):
    CO=[[0]]
        
    for n in range(1,N):
        CO.append([])
        for k in range(0,min(K,int(n*(n-1)*0.5))+1):
            tmp2=kf[n][k]*binomial(n, K-k)*binomial(N+K-n-k-1,K-k-1)
            CO[n].append(tmp2)
            CO[0][0]=CO[0][0]+tmp2
    return CO



def recursive_generator(N):

    taille=[int(pow(N,0.5)),
            int(math.log(N)),
            N,
            int((N-2)*(N-3)*0.5),
            int(N/2)
		]
    #taille=[N]
    elem=[]
    res=[]
    res2=[]
    nb_ok=1
    ind=0
    moy=100
    for e in taille:
        print 'nouveau'
        elem.append([])
        res.append([])
        res2.append([])
        #for r in range(0,int(N*(N-1)*0.5)+1):
        for r in range(0,N+1):
            elem[ind].append(0)
            res[ind].append(0)
            res2[ind].append(0)
            nb_ok=1
            #calcul origine de l arbre 
        while nb_ok<=moy:
            print '%d' % nb_ok
            if(nb_ok % 50==0):
                print '%d' % nb_ok
            to=un_arbre(N,e)
         #   print 'recur to[1] %s' % to[1]
            noeuds=recon_arbre(to[1])
          #  print 'arbre non %s' % str(noeuds)
          #  print 'arbre apres %s' % str(elaguer_arbre(noeuds))
          #a decommenter pour elegage
          #  resdeg=[0 for i in range(N+1)]
          #  degree_arbre(elaguer_arbre(noeuds),resdeg)
          #  ajout_res(res[ind],resdeg)
          #  print 'degree %s' % str(resdeg)
           # print 'recur %s' % str(noeuds)
           # noeuds2=recon_arbre(noeuds)
            ajout_res(res[ind],to[0])
           
          #  print '%s' % str(res)
            nb_ok=nb_ok+1
            for z in range(0,len(elem[ind])):
                elem[ind][z]=0
                #    n=n+1
           # taille=taille + height(noeuds2)
        nb_ok=nb_ok-1
      #  print 'res %s' % str(res)
        for z in range(0,len(res[ind])):
            res2[ind][z]=res[ind][z]/float(nb_ok)
        ind=ind+1
        
        # prob=0
        # for cv in range(2,len(res[0])):
        #     prob=prob+res[0][cv]
        # print 'proba avant %d' % prob
        # print 'prob %f' % (prob/float(nb_ok))
        #tabtaille.append(taille/float(nb_ok))
        nb_ok=1
        print 'fini'
    print '# moyenne sur %d taille %d' % (moy,N)
    for yu in range(0,len(res2[0])):
        y= " "
        x=[str(yu+1)]
        for i in range(0,len(taille)):
            x.append(str(res2[i][yu]))
        print '%s' %  y.join(x) 
       
    return res2


def un_arbre(t,k):
  #  print 'un arbre %d %d' % (t,k)
    noeuds=[]
    to=[]
    for r in range(0,t+1):
        to.append(0)
    n=random.randint(1,getkf(t,k))
    trouverarbre(n,t,k,to,noeuds)
    return [to,noeuds]

def getkf(t,k):
    denom.seek(0,0)
    for i in range(0,t):
        x=denom.readline()
    x=x.split(',')
    x.pop()
    x = list(map(int, x))
    return x[k]



def getco(t,k):
    ind.seek(0,0)
    for i in range(0,t):
        x=ind.readline()
    x=x.split(',')
    x.pop()
    x = list(map(int, x))

    cof.seek(x[k],0)
    
    while True:
        c=cof.read(1)
        if(c==';'):
            break
        res=string.join([res,c],"")
    y=res.split("!")
    y=pop()
    for e in y:
        e=e.split(',')
        e.pop()
        e = list(map(int, e))
  
        res.append(e)
  
    return res



def elaguer_arbre(arbre):
#    print 'elaguer %s' % str(arbre)
    if(arbre is None):
        print 'a voir'
        return []
    fils=[]
    for e in arbre[2]:
        if not(e[2] is None):
            fils.append(elaguer_arbre(e))
    return [arbre[0],arbre[1],fils]

def degree_arbre(arbre,res):
    if arbre[2]==[]:
        return
    for e in arbre[2]:
        degree_arbre(e,res)
    res[len(arbre[2])-1]=res[len(arbre[2])-1]+1
    


def gene_dot(noeuds):
    fil = open("essai.gv",'w')
    fil.write("digraph G {\n")
    ecrit(fil,noeuds)
    

    fil.write("}\n")

def ecrit(fil,noeuds):
   # print 'ecrit %s' % noeuds
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
   # print 'recon %s' % str(noeuds)
    id=[2]
    abr=initialistation(noeuds[len(noeuds)-1],id)
    rac=[1,1,abr]

    for fg in range(1,len(noeuds)):
       # print 'ahhhhhhhhhh %d' % len(noeuds)
        j=len(noeuds)-1-fg
        for k in range(0,len(noeuds[j])):
            if not(noeuds[j][k]==None):
        #        print 'noeuds j k %s' % noeuds[j][k]
                etendre(k,noeuds[j][k],rac,fg+1,id)
   # print 'cloche %s' % str(rac)
    return rac
            


def etendre(k,ari,rac,lab,id):
    # print 'etendre k %d' % k
    # print 'etendre arite %d' % ari
    # print 'etendre %s' % str(rac)
    x=trouver_feuille(k,rac)
    etendre_feuille(x,ari,lab,id)


def etendre_feuille(x,ari,lab,id):
    # print 'etendref %s' % str(x)
    # print 'etendref arite %d' % ari
    # print 'etendref lab %d' % lab
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
    # print 'trouver_feui n %d' % n
    # print 'trouver_feu noeuds %s' % str(noeuds)
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
                
            

    
N=int(sys.argv[1])

#K=int(sys.argv[3])
#cal_coeff(N,int(N*(N-1)*0.5))
#lire_coeff(N)

if(sys.argv[2]=='1'):
    recursive_generator(int(sys.argv[1]))
else:
    
   if(int(sys.argv[3])>int(sys.argv[1])):
       print 'taille arbre demande plus grande que possible'
   else:
       print 'good'

       coq=un_arbre(int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[1]))
       # for e in coq:
       #     print '\n'
       #     for i in e :
       #         if not(i==None):
       #             print '%d,' % i
       #         else:
       #             print '*,'
       print 'coq %s fini' % str(coq)
       noeuds2=recon_arbre(coq)
       gene_dot(noeuds2)


