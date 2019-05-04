# Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Informe: '))
r2 = float(input('Informe: '))
r3 = float(input('Informe: '))
if r1 < r2+r3 and r2 < r1 + r3 and r3 < r2+r1:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem formar triângulo')