# -*- coding: utf-8 -*-
"""Soma_dos_Dígitos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jZcK-Ukwwok8gOrFZY27wqtmfVb3MDws
"""

x = int(input("Digite um número inteiro: "))

soma = 0

while x > 0:
    resto = x % 10
    x = x // 10
    soma = soma + resto

print(soma)