# -*- coding: utf-8 -*-
"""Distancia_Entre_Dois_Pontos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8k9dbxYCA1n6p33jnGMIpx1SKDtLyAF
"""

import math

def distanciaDeDoisPontos(x1,y1,x2,y2):
  distanciaDeDoisPontos = ((x1- x2)**2) + ((y1-y2)**2)
  return math.sqrt (distanciaDeDoisPontos)

print(' ----------- Distância entre dois pontos ----------- \n')

x1 = int(input('digite o ponto: '))
y1 = int(input('digite o ponto: '))
x2 = int(input('digite o ponto: '))
y2 = int(input('digite o ponto: '))

if(distanciaDeDoisPontos(x1,y1,x2,y2) > 10):
  print('longe')
else:
  print('perto')