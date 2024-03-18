# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:39:25 2024

@author: brenda santana

aula de python inicial - fundamentos de big data
"""
import statistics

#### Operadores Aritmeticos

#comando para mostrar mensagem
print("Alo mundo")

#comando para inserir valores
b = input("Digite um número ou uma palavra:")

#comando para atribuir valor a variavel
a = int(input("digite um numero: "))

#mostrando variaveis
print(a, b)
print(type(a), type(b))

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))

#soma de variaveis
s = (x + y)
print("A soma dos valores informados é:", s)

#mudando tipo da variavel
a = input("Digite um número: ")
print(type(a))
b = int(a)
print(type(b))


### Estrutura de decisão
n1= int(input("Digite a média do aluno: "))
if n1 >= 7:
    print("Aprovado!!")
else:
    print("Reprovado!!!")
    
    
### Estrutura de repetição
count = 1
while count <= 5:
    print(count)
    count += 1
    
for n in range(0,10):
    print(n)
    
### Listas

lista = [ ] #vazio
lista1 = [1, 3, 4, 5, 'lili', 5.11]


print(lista1)

sm = [1, 3, 4, 5, 'lili', 5.11]
sm.append('jose')
print(sm)

### tupla

tupla = (1, 2, 3)
lista = list(tupla)

### dicionario

preco = {'lapis': 5.5, 'borracha': 7.0}

preco ['caneta'] = 10.0
del preco ['borracha']

### verificando tamanho do vetor

tamanho_preco = len(preco)

### valor maximo de um arquivo

x = max(5, 10, 25)

### valor minimo de um arquivo

minimo = [1, 2, 3, 4, 5]
menor_valor = min(minimo)

### Arredondando o valor da variavel

numero = 3.141511231
numero_arredondado = round(numero)

### calculos aritmeticos

lista = [1, 2, 3, 4, 5]
media = statistics.mean(lista)
mediana = statistics.median(lista)
