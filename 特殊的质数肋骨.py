from math import sqrt    
      
def Isprime(x):    
    if x < 2:    
        return False    
    else:    
        for i in range(2,int(sqrt(x)+1)):    
            if x % i == 0:    
                return False    
    return True    
      
def f(a,count,n):    
    if count == n:    
        print(a)    
    else:    
        for item in [1,3,7,9]:    
            temp = a*10 + item    
            if Isprime(temp):    
                f(temp,count+1,n)

n = int(input())    
f(2,1,n)
f(3,1,n)    
f(5,1,n)    
f(7,1,n)
