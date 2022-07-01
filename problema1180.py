# Problema 1180

# pegando o input
n = int(input())

# criando a lista
x = []
a = list(map(int, input().split()))

# denominando a lista
for i in range (n):
    x.insert(i, a[i])

# output
print("Menor valor: %d" %(min(x)))
for i in range(n):
    if x[i] == min(x):
        pos = i
print("Posicao: %d" %pos)