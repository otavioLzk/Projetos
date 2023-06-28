""" Codifique um algoritmo que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem: 19, 21, 25, 22, 20, 17 e 15ºC, de domingo a sábado, respectivamente, o algoritmo deverá exibir:
D: *******************
S: *********************
T: *************************
Q: **********************
Q: ******************
S: *****************
S: ***************
Suponha que as temperaturas sejam todas positivas até 80ºC.
"""
import random

dias = ['D', 'S', 'T', 'Q', 'Q', 'S', 'S']
temperaturas = []

for i in range(0,7):
    temperaturas.append(random.randint(0,80))


for i in range(0,len(dias)):
    print(f'{dias[i]}: ', '*' * temperaturas[i])
    temperaturas[i] = str(temperaturas[i])

print(f'As temperaturas foram '+ ', '.join(temperaturas) +'ºC, respectivamente.')