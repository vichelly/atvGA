print("Versor de um Vetor:")
print("Coordenadas do vetor:")
a = float(input("Digite a 1a. coordenada: "))
b = float(input("Digite a 2a. coordenada: "))
c = float(input("Digite a 3a. coordenada: "))
div = (((a*a)+(b*b)+(c*c))**(0.5))
print("Versor: 1/{:.2f} ({:.2f}, {:.2f}, {:.2f})".format(div,a,b,c))
print("Versor: ({:.2f}, {:.2f}, {:.2f})".format(a/div,b/div,c/div))
