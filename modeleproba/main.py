import sys
import string
import arbre

#number of steps of construction
N=int(sys.argv[1])
alpha=float(sys.argv[2])


def main():
    cmp=0
    while(cmp<10):
        res=[]
        arbre.un_arbre(N,alpha,res)
        print res
        res2= arbre.recon_arbre(res)
        print res2
        cmp=cmp+1
    

main()
