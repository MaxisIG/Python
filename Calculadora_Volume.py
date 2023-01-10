import math

class Calculadora:
    def cilindro(raio,altura):
        volume = math.pi * math.pow(raio,2) * altura
        print(volume)
    def cubo(lado):
        volume = math.pow(lado, 3)
        print(volume)
    def esfera (raio):
        volume = ((4/3)*math.pi) * math.pow(math.pi,3)
        print(volume)
x1 = Calculadora
x = input("Calculo de volume, digite A para cilindro, B para cubo e C para esfera: ").upper()
while(True):
    if x == 'A':
        raio = int(input("Digite o valor do raio do cilindro: "))
        altura = int(input("Digite o valor da altura do cilindro: "))
        x2 = x1.cilindro(raio,altura)
        x = input("Para calcular outro volume digite A, B ou C, se quiser encerrar digite D: ").upper()
    elif x == 'B':
        lado = int(input("Digite o valor do lado do cubo: "))
        x2 = x1.cubo(lado)
        x = input("Para calcular outro volume digite A, B ou C, se quiser encerrar digite D: ").upper()
    elif x == 'C':
        raio = int(input("Digite o valor do raio da esfera: "))
        x2 = x1.esfera(raio)
        x = input("Para calcular outro volume digite A, B ou C, se quiser encerrar digite D: ").upper()
    elif x == 'D':
        break
    else:
        print("Por favor digitar apenas A, B ou C, se quiser encerrar digitar D.")
        x = input("Para calcular outro volume digite A, B ou C, se quiser encerrar digite D: ").upper()

