print("ADIÇÃO DE MATRIZES: ")
lm = int(input("Digite o número de linhas  da matriz M: "))
cm = int(input("Digite o número de colunas da matriz M: "))

M = []

for i in range(lm):
    linem = []
    for k in range(cm):
        elementm = input("Digite o elemento {} {} da matriz: ".format(i+1,k+1))
        linem.append(float(elementm))
    M.append(linem)

print()
ln = int(input("Digite o número de linhas  da matriz N: "))
cn = int(input("Digite o número de colunas da matriz N: "))

N = []

for i in range(ln):
    linen = []
    for k in range(cn):
        elementn = input("Digite o elemento {} {} da matriz: ".format(i+1,k+1))
        linen.append(float(elementn))
    N.append(linen)

S = []
if (lm == ln) and (cm == cn):
    for i in range(lm):
        linha = [0]*cm
        S.append(linha)
        for k in range(cm):
            S[i][k] = M[i][k] + N[i][k]

    for i in range(ln):
        for k in range(cn):
                print(S[i][k], end = " ")
        print()
                    
else:
    print("Matrizes Incompatíveis.")

