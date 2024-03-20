##testando conexao com banco de dados
#fazendo importação da biblioteca do postgre para o python
import psycopg2

#fazendo a conexao com o banco de dados criado no postgre 'senai'
#host, banco de dados, usuario, senha e porta
connection = psycopg2.connect(host = "127.0.0.1", database = "senai", user = "postgres", password = "senai", port = "5432")

#criando uma classe 'cursor' para chamar comandos para o banco de dados
cursor = connection.cursor()

##modificando o banco de dados
#inserindo dados no banco uma informaçao nova
insert = "INSERT INTO clientes(cliente, estado, sexo, status) VALUES('Lílian de Paula', 'SP', 'F', 'Obsidian')"

#executando o comando informado
cursor.execute(insert)

#salvando as alterações no banco de dados
connection.commit()

##testando comandos
queryMostrar = "SELECT * FROM clientes"
cursor.execute(queryMostrar)

#chamando os dados lidos no cursor e guardando no array registro
registro = cursor.fetchall()

##exemplo de menu
controller = 0
while(controller != 9):
    controller = (int(input("MENU PRINCIPAL \n1- select \n2- insert \n9- sair \n-> ")))
    if(controller == 1):
        query = input("\n-> ")
        cursor.execute(query)
    elif(controller == 2):
        insert = input("\n-> ")
        cursor.execurte(insert)
        connection.commit()
    elif(controller != 1 and controller != 2 and controller != 9):
        print("\nComando inválido!")
    else:
        controller = 9
       
#fechando processos
cursor.close()
connection.close()