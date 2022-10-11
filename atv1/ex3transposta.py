lm = int(input("Digite o número de linhas  da matriz M: "))
cm = int(input("Digite o número de colunas da matriz M: "))

M = []

for i in range(lm):
    linem = []
    for k in range(cm):
        elementm = input("Digite o elemento {} {} da matriz: ".format(i+1,k+1))
        linem.append(float(elementm))
    M.append(linem)

print("MATRIZ")
for i in range(lm):
    for k in range(cm):
            print(M[i][k], end = " ")
    print()
print()
print("MATRIZ TRANSPOSTA:")
MT = [[0 for j in range(lm)] for i in range(cm)]

for i in range(lm):
    for j in range(cm):
        MT[j][i] = M[i][j]

for i in range(cm):
    for k in range(lm):
            print(MT[i][k], end = " ")
    print()

