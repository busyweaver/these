import math
import random
import sys
import string

bino={}

f = open(sys.argv[1]+"_coeff"+".txt", 'w')
g = open(sys.argv[1]+"_denom"+".txt", 'w')
ind = open(sys.argv[1]+"_index"+".txt", 'w')
f.write('1,!;\n')
g.write('1,\n')


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
        CON.append([0])
        kf.append([])
        for k in range(0, int((n)*(n-1)*0.5)+1):
            ind.write(str(f.tell())+",")
            tmp = calcul_CO(n,kf,k)
            kf[n].append( tmp[0][0])
            g.write(str(tmp[0][0])+",")
           
            tmp[0][0]=0
         #   if(sys.argv[2]=='1' or sys.argv[2]=='2'):
        g.write('\n')
        f.write('\n')
        ind.write('\n')

   
       
def calcul_CO(N,kf,K):
    CO=[[0]]
    if(K==0):
        f.write(str(0))
        f.write(',!')
        f.write(';')
        return [[0]]
        
    for n in range(0,N):
        CO.append([])
        for k in range(0,min(K,int(n*(n-1)*0.5))+1):
            tmp2=kf[n][k]*binomial(n, K-k)*binomial(N+K-n-k-1,K-k-1)
            #if(tmp2!=0):
            f.write(str(tmp2))
            f.write(',')
            CO[0][0]=CO[0][0]+tmp2
        f.write('!')
    
    f.write(';')
    return CO

cal_coeff(N)
g.close()
f.close()     
ind.close()
