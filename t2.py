def fibo(n):
    
    if n <= 0 or n == 1:
        return 1

    else:
        return float(fibo(n-2)+fibo(n-1))

def luku(n):
    return float((fibo(n-1)/fibo(n)))
    
print luku(0)
print luku(3)
print luku(5)
