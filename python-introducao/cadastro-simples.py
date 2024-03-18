# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:02:35 2024

@author: brenda santana

aula de python inicial - fundamentos de big data - cadastro simples

"""

perfil = [[],[],[],[],[]] ##lista com dados do usuario
trava = 1; #variavel que mantera adicionando novos usuarios
while True:
    #adquirindo dados
    nome = str(input("Insira o seu nome: "))
    perfil[0].append(nome) #adicionando nome
    
    sobrenome = str(input("Insira o seu sobrenome: "))
    perfil[1].append(sobrenome) 
    
    telefone = int(input("Insira o seu telefone: "))
    perfil[2].append(telefone) 
    
    idade = int(input("Insira a sua idade: "))
    perfil[3].append(idade) 
    
    estado = str(input("Insira o seu estado: "))
    perfil[4].append(estado)
    cons = input("Deseja cadastrar:\ns - Sim\nn - Não\n ")
    if cons == 'n':
        print("Fim do Cadastro.")
        break
    
while True:
    cons = input("Deseja consultar cadastro:\ns - Sim\nn - Não\n ")
    if (cons != 's'):
        break
    else:
        nome = str(input("Insira um nome que deseja pesquisar: "))
        if nome in perfil[0]:
            print(f"Nome encontrado : {perfil[0][perfil[0].index(nome)]}")
        else:
            print("Nome ", nome," não encontrado!")
            
while True:
    op = input("Deseja excluir um registro?\ns- Sim\nn - Não\n ")
    if op != "n":
        nom = input("Digite o nome: ")
        if nome in perfil[0]:
            perfil[0].remove(nom)
            print(f"Nome removido: {nom}")
            print(f"{perfil[0]}")
        else:
            break
    else:
        break
            