# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:42:49 2024

@author: brenda santana

aula de python inicial - fundamentos de big data - media aluno
"""

#adquirindo variaveis
n1 = int(input("Digite a primeira nota do aluno: "))
n2 = int(input("Digite a segunda nota do aluno: "))
n3 = int(input("Digite a terceira nota do aluno: "))
#calculo de media
media = (n1 + n2 + n3) / 3
#condicao
if media > 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Conselho!!")
else:
    print("Reprovado!!!")    
