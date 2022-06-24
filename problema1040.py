# Problema 1040

# inputar as notas
nA, nB, nC, nD = input().split()
nA = float(nA)
nB = float(nB)
nC = float(nC)
nD = float(nD)

# valor dos pesos
pA = 2
pB = 3
pC = 4
pD = 1
p = pA + pB + pC + pD

# calcular as médias
m = ((nA*pA)+(nB*pB)+(nC*pC)+(nD*pD))/p

# mostrando o valor da média
print(f"Media: {m:.1f}")

# condicionais
if m >= 7.0:
    print("Aluno aprovado.")
elif m < 5.0:
    print("Aluno reprovado.")
elif m >= 5.0 and m < 7.0:
    print("Aluno em exame.")
    nR = float(input())
    mF = (nR+m)/2
    print(f"Nota do exame: {nR:.1f}")
    if mF >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mF:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {mF:.1f}")