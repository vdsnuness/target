# -*- coding: utf-8 -*-
"""Exercicio_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bO2wKDDMIAOIQpYWu5YLsotTO1xHuR7q
"""

seq = [1,1]
i = 0
num = int(input("Digite um valor: "))

while num > len(seq):
	seq.append(seq[i] + seq[i+1])
	i+=1

print ('Sequência de Fibonacci(%d): %d' %(num,seq[num-1]))