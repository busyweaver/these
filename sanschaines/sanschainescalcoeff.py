import math
import random
import sys
import string
noeuds=[]
bino={}
compo={}
com1=1


f = open(string.join([sys.argv[1]],'_')+".txt", 'w')

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

N=int(sys.argv[1])
kf = [[0],[1,0]]


CON=[
    [0],
    [ [[1],[0]]       ]
    

]

def cal_coeff(N):
    for n in range(2,N+1):
        print 'n!===========%d' % n
        f.write('\n')
        CON.append([0])
        kf.append([0])
        for k in range(1, n):
            tmp = calcul_CO(n,kf,k)
            kf[n].append( tmp[0][0])
            tmp[0][0]=0
            f.write(str(tmp))
            f.write(',')
         #   if(sys.argv[2]=='1' or sys.argv[2]=='2'):
        f.close()
         
       
def calcul_CO(N,kf,K):
    CO=[[0]]
        
    for n in range(1,N):     
        CO.append([])
        for k in range(0,n):
            tmp2=kf[n][k]*binomial(n, K-k)*binomial(N-n-1,K-k-1)
            CO[n].append(tmp2)
            CO[0][0]=CO[0][0]+tmp2
    return CO

cal_coeff(N)
