# -*- coding: utf-8 -*-
"""Exercicio_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bO2wKDDMIAOIQpYWu5YLsotTO1xHuR7q
"""

from pickle import STRING
sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
out = float(19.84953)

total = float(sp + rj + mg + es + out)
print(total)

porcSp = ((sp*total)/100)
porcRj = ((rj*total)/100)
porcMg = ((mg*total)/100)
porcEs = ((es*total)/100)
porcOut = ((out*total)/100)

print('Porcentagem de SP {}'.format(porcSp))
print('Porcentagem de RJ {}'.format(porcRj))
print('Porcentagem de MG {}'.format(porcMg))
print('Porcentagem de ES {}'.format(porcEs))
print('Porcentagem de OUT {}'.format(porcOut))