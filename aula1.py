import datetime 

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


#print(fibonacci(40))

def fibonacci2(n):
   
    vetor = [0] * (n + 1)
    vetor[0] = 0
    vetor[1] = 1

    for x in range(2,n+1,1):
        vetor[x] = vetor[x-1] + vetor[x-2]

    return vetor[n]

print(fibonacci2(45))