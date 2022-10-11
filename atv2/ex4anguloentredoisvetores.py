from math import acos
from math import degrees

print("Ângulo entre os vetores u e v:")
print("Coordenadas do vetor u:")
ux=float(input("Digite a 1a. coordenada: "))
uy=float(input("Digite a 2a. coordenada: "))
uz=float(input("Digite a 3a. coordenada: "))
print("Coordenadas do vetor v:")
vx=float(input("Digite a 1a. coordenada: "))
vy=float(input("Digite a 2a. coordenada: "))
vz=float(input("Digite a 3a. coordenada: "))

div_u=(((ux*ux)+(uy*uy)+(uz*uz))**(0.5))
div_v=(((vx*vx)+(vy*vy)+(vz*vz))**(0.5))

multi_vet=((ux*vx)+(uy*vy)+(uz*vz))
mult_mod_vet=(div_u*div_v)
final=multi_vet/mult_mod_vet
rad=acos(final)
angulo=degrees(rad)
print("Ângulo: {:.2f}".format(angulo),"graus")