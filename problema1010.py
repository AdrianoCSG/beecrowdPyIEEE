# Problema 1010

# pegando os 3 primeiros inputs
prodA, quantA, valA = input().split()
prodA = int(prodA)
quantA = int(quantA)
valA = float(valA)

# pegando os 3 segundos inputs
prodB, quantB, valB = input().split()
prodB = int(prodB)
quantB = int(quantB)
valB = float(valB)

# definindo os cálculos
resA = valA * quantA
resB = valB * quantB
res = resA + resB

# printando o output corretamente
print("VALOR A PAGAR: R$ {:.2f}".format(res))