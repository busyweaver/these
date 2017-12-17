import math
import random
import sys
import string

#partition ensemble en k classe, ordered striling number of second kind


def maxi(t):
    if (len(t)==0):
        return (-1,-1,-1)
    max=t[0]
    arg=0
    for i in range(1,len(t)-1):
        if(t[i]>max):
            max=t[i]
            arg=i
    return (max,arg,len(t))


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



plus=[[],[],[]]
moins=[[],[],[]]
res=[]


kf = [[0],[0,1],[0,1,2]]
coeff=[0]
D=int(sys.argv[1])

for n in range(1,D-2):
    kf.append([0,1])
    plus.append([[],[],[]])
    moins.append([[],[],[]])




# for n in range(3,D):
#     if(n%50==0):
#         print '%d' % n
#     for k in range(2,n+1):
#         kf[n].append(sum(   kf[r][k-1]*r  for r in range(k,n) ) )

for n in range(3,D):
    if(n%50==0):
        print '%d' % n
    for k in range(2,n+1):
        plus[n].append([])
        moins[n].append([])
        tmp=0
        for j in range(0,k+1):
            tmp2=binomial(k,j)*pow(j,n)
            if(pow(-1,k-j)==1):
                plus[n][k].append(tmp2)
                tmp=tmp+tmp2
            else:
                moins[n][k].append(tmp2)
                tmp=tmp-tmp2
        kf[n].append(tmp)
                
    kf[n].append(sum(       pow(-1,k-j)*binomial(k,j)*pow(j,n)    for j in range(0,k+1)))
    

        
for i in range(1,D):
    m=-1
    arg=-1
    for j in range(1,len(kf[i])):
        #print '%d' % kf[i][j] 
        if(kf[i][j]>m):
            m=kf[i][j]
            arg=j
  #  print '%d : %d,%d,%d' % (i,arg,2*math.exp(-1)*i-1,(float(1)/float(math.exp(1) - float(math.pow((1 + (1/float(i))),i))))-1)
    print '%d : %d,%d,%f,%f' % (i,arg,2*math.exp(-1)*i-1,float(arg)/float(i),sum(kf[i])//m)
            
for n in range(3,D):
    x=maxi(kf[n])
    print 'n %d,%d,%d,%f,%f' % (n,x[1],math.floor(0.5*((n+3)/math.log(2))-1),(x[1]/float(n)),n-math.log(n))

print '%f' % math.log(2)

for i in range(0,len(kf[D-2])):
    print '%d  %f,' % (i,(kf[D-2][i]/float(sum(kf[D-2]))))
#print '%s' % str(kf[D-2])
#print '%d' % sum(kf[D-2])

# d=[1]
# for n in range(1,D):
#     d.append(sum(kf[n][k] for k in range(0,len(kf[n]))))

# print 'bd = %s' % str(d)
# for i in range(0,D-1):
#     print 'n%d,' % (0.25*d[i+1]-0.75*d[i]) 


# for i in range(0,D):
#     print '%d,' % sum((0.5*k-0.5)*kf[i][k] for k in range(0,len(kf[i])))
