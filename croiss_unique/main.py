import cfu
import sys
import string
import prm
import trans
N=int(sys.argv[1])
recur = [0,1]
recurint=[
    [0],
    [1]
    ]


def triangle_hauteur(N):
    ren=[]
    for i in range(2,N+1):
        haut = [0 for j in range(0,N)]
        res=cfu.iterateur(i,recur,recurint)
        for e in res:
            #print e
            res2 = trans.recon_arbre(e)
            #print res2
            h = trans.hauteur(res2)
            haut[h]=haut[h]+1
        ren.append(haut)
    return ren
    
def nbdescente_perm(N):
    ren=[]
    for i in range(2,N+1):
        haut = [0 for j in range(0,N)]
        res=prm.perm_contr(i,1,2)
        for e in res:
            #print e
            #print res2
            h = prm.nb_descente(e)
            haut[h]=haut[h]+1
        ren.append(haut)
    return ren

def triangle_noeuds(N):
    ren=[]
    for i in range(2,N+1):
        haut = [0 for j in range(0,N)]
        res=cfu.iterateur(i,recur,recurint)
        for e in res:
            #print e
            res2 = trans.recon_arbre(e)
            #print res2
            h = trans.nombre_noeuds(res2)
            #print h
            haut[h]=haut[h]+1
        ren.append(haut)
    return ren

def main():

    # tab=[]
    # res2=[]
    # perm=prm.perm_contr(N,1,2)
    # for e in perm:
    #     res=prm.profil(e)
    #     print res
    # for e in res:
    #     print e 
    #     trans.permtoarb(e,tab)
    #     print 'allee'
    #     print tab
    #     print 'retour'
    #     trans.arbtoperm(tab,res2)
    #     print res2
    #     print ''
    #     res2=[]
    #     tab=[]
    # print 'fin'
    cfu.recurrence(N,recur,recurint)
    res=cfu.iterateur(N,recur,recurint)
    for e in res:
        print e
        res2=cfu.recon_arbre(e)
        print res2
    #print res
    
    # haut=[[] for i in range(0,N)]
    # for e in res:
    #     pr=[]
    #    # print e
    #     # trans.arbtoperm(e,pr)
    #     # res2=trans.recon_arbre(e)
    #     # h=trans.hauteur(res2)
    #     # haut[h].append(pr)
    #     #print res2
        
    # # for j in range(0,len(haut)):
    # #     print j
    # #     for i in haut[j]:
    # #         print i

    # res = triangle_hauteur(N)
    # for e in res:
    #     for g in e:
    #         print g
    
    
    #res = nbdescente_perm(N)
    #print res
    #print "%s" % str(recurint)
    #print "%s" % str(recur)
    
    #arbrefor=cfu.un_arbre(int(sys.argv[1]),recur,recurint)
    #print arbrefor
    #res=trans.recon_arbre(arbrefor)
    #print res
    #arbre=cfu.recon_arbre(arbrefor)
#    gene_dot(arbre)

# if(sys.argv[2]=='0'):
#     cal_coeff()
#     sauv_coeff()

# elif(sys.argv[2]=='1'):
#     cal_coeff()
#     print 'kf %s' % str(kf)
#     moy=recursive_generator(int(sys.argv[1]))
# #    print 'res %s' % str(moy[0])
    
# else:
    
#    if(int(sys.argv[3])>int(sys.argv[1])):
#        print 'taille arbre demande plus grande que possible'
#    else:
#        print 'good'
#        cal_coeff()
#        print 'Co %s' % str(CON[5])
#        coq=un_arbre(int(sys.argv[3]))
#        # for e in coq:
#        #     print '\n'
#        #     for i in e :
#        #         if not(i==None):
#        #             print '%d,' % i
#        #         else:
#        #             print '*,'
#        print 'coq %s' % str(coq)
#        noeuds2=recon_arbre(coq)
#        taille=height(noeuds2)
#        print 'taille %d' % taille
#        print 'arbre %s' % str(noeuds2)
#        gene_dot(noeuds2)

main()


    
