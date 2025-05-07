import datetime 

#fibonacci tradicional com recursividade
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


#print(fibonacci(40))

#fibonacci de forma dinamica utilizando lista para armazenar os valores
def fibonacci2(n):
   
    vetor = [0] * (n + 1)
    vetor[0] = 0
    vetor[1] = 1

    for x in range(2,n+1,1):
        vetor[x] = vetor[x-1] + vetor[x-2]

    return vetor[n]

#fibonacci implementando uma tabela hash
def fibonacci3(n):

    if n == 0 or n == 1:
        return n

    if n in vetorHash.keys():
        return vetorHash[n]
    vetorHash[n] = fibonacci3(n-1) + fibonacci3(n-2)
    return vetorHash[n] 


vetorHash = {}
vetorHash[0] = 0
vetorHash[1] = 1

print(fibonacci3(100))