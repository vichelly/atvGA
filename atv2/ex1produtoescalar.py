print("Produto Escalar: ")
d = int(input("Digite a dimensão dos vetores: "))
u = []
v = []
print("Coordenadas do vetor u:")
for i in range(d):
    aux = float(input("Digite a {}a. coordenada: ".format(i+1)))
    u.append(aux)
print("Coordenadas do vetor v:")
for i in range(d):
    aux = float(input("Digite a {}a. coordenada: ".format(i+1)))
    v.append(aux)

def prodesc(u,v):
    mult = []
    for i in range(len(u)):
        m = u[i] * v[i]
        mult.append(m)
    resp = sum(mult)
    print("Produto Escalar: {:.2f}".format(resp))
            

prodesc(u, v)
