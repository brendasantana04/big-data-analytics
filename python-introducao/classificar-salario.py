# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:20:09 2024

@author: brenda santana 

aula de python inicial - fundamentos de big data - media aluno

"""

## definindo salario minimo
salario =  float(1412)

##adquirindo dados do usuario
salUsuario= float(input("Insira o seu salário atual: "))

##definindo classe do usuário

if (salUsuario >= (salario * 10)):
    print("Classe alta")
elif (salUsuario >= (salario * 5)):
    print("Classe media")
else:
    print("Classe baixa")    