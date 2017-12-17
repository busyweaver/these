

def trouver_coeff_somme(n,CO):
    #verifier somme i ou 2 dimension
    if(type(CO[m]) is list):
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

        
    else:
        ab=n
        m=len(CO)-1
        while (ab>0):
            ab=ab-CO[m]
            m=m-1
            
        m=m+1
        ab=ab+CO[m]

        return [m,ab]



def getcoeffrecur(n,k=-1,fil,kf):
    if (len(kf)>n):
        if (k==-1):
            return kf[n]
        else:
            return kf[n][k]
    else:
        if(k==-1):
            fil.seek(0,0)
            fil.read()
            fil.split(',')
            fil.pop()
            x = list(map(int, x))
            return x[n]

        else:
            fil.seek(0,0)
            for i in range(0,t):
                x=fil.readline()
            x=x.split(',')
            x.pop()
            x = list(map(int, x))
            return x[k]

def getcoeffinterne(n,k=-1,fil,CO,ind):
        if (len(CO)>n):
            if (k==-1):
                return CO[n]
            else:
                return CO[n][k]
        else:
            if(k==-1):

            else:
                ind.seek(0,0)
                for i in range(0,t):
                    x=ind.readline()
                x=x.split(',')
                x.pop()
                x = list(map(int, x))
                fil.seek(x[k],0)
    
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

            


################## transformer arbre representation tableau vers arbre #################




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



################# dessiner arbre ##################


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
            

################# generateur recursif #########################


def un_arbre(t,noeuds):
    profil=[]
    arbre=[]
    for r in range(0,int(t*(t-1)*0.5)+1):
        profil.append(0)
    n=random.randint(1,kf[t])
    trouverarbre(n,t,kf,profil,arbre)
    return (profil,arbre)


def recursive_generator(N,nbarbre):
    accum=[]
        while nb_ok<=nbarbre:
            if(nb_ok % 100==0):
                print '%d' % nb_ok
            res=un_arbre(N,elem[ind])
           # print 'recur %s' % str(noeuds)
           # noeuds2=recon_arbre(noeuds)
            ajout_res(res[0],accum)
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
        print 'fini'
    for yu in range(0,21):
        print '%d %f' % (yu+1,res2[ind][yu])
   # for fg in range(0,len(tabtaille)):
    #    print '%d %f' % (((9-fg+1)*5),tabtaille[fg])
    return res2

def ajout_res(res,elem):
    for z in range(0,len(res)):
        res[z]=res[z]+elem[z]


def evol_nbnoeuds(N):

    return 0

def evol_hauteur(N):

    return 0


def moyenne_aritenoeuds(N):
#profil de l arbre
    return 0

def moyenne_nbnoeuds(N):

    return 0



def hauteur(arbre):
    maxi=[]
    if(arbre[2]==None):
        return 0
    for df in arbre[2]:
        maxi.append(height(df))
    return 1+max(maxi)


############################## utilitaires ###########################

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

bino={}
  
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

