# Problema 1019

# coletando o número
s = int(input())

# realizando os cálculos
m = int(s/60)
s -= m*60
h = int(m/60)
m -= h*60

# output
print(f"{h}:{m}:{s}")