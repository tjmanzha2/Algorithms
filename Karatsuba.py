import math

def recIntMult(A, B):
    n = int(math.log10(A)) + 1 # power of the multiplicand
    if n == 1 :
        return A*B
    
    else :
        m = int(n/2)
        a = int(A / math.pow(10, m)) 
        b = int(A % math.pow(10, m)) 
        c = int(B / math.pow(10, m)) 
        d = int(B % math.pow(10, m)) 
        ac = recIntMult(a,c)
        bd = recIntMult(b,c)
        adbc = recIntMult(a+b, c+d) - ac - bd
        multResult = math.pow(10, n)*ac + bd + math.pow(10, m)*adbc 
        return multResult

if __name__ == "__main__" :
    A = 3214
    B = 1545
    multInt = recIntMult(A, B)
    print(multInt)