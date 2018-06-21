import math
import random
import sys
import string

##https://rosettacode.org/wiki/Ordered_Partitions#Python
from itertools import combinations
 
def partitions(*args):
    def p(s, *args):
        if not args: return [[]]
        res = []
        for c in combinations(s, args[0]):
            s0 = [x for x in s if x not in c]
            for r in p(s0, *args[1:]):
                res.append([c] + r)
        return res
    s = range(sum(args))
    return p(s, *args)


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


def ordered_partition(n):
    res=[]
    for i in range(1,n+1):
        l=composition(n,i)
        for e in l:
            #print e
            tmp=tuple(e)
            #print partitions(*tmp)
            res = res + partitions(*tmp)
    return res



    
