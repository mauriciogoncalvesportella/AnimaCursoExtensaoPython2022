#Primeiro passo: importar a biblioteca sqlite3

import sqlite3

#Segundo passo: Vamos estabelecer uma conexão com o banco de dados

conexao = sqlite3.connect('dc_universe.db')

#Terceiro passo: Criar um objeto do tipo cursos
cursor = conexao.cursor()

#Quarto passo: comando SQL do banco
sql = 'SELECT pessoa_id, nome, nome_civil, tipo FROM  pessoas'

#Quinto passo: executar o comando SQL no SQLite (no cursor)
cursor.execute(sql)

#Sexto passo: exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall() # fetchall é para pegar toda a informação
for pessoa in pessoas:
  print(f'Nome: {pessoa[1]} ({pessoa[3]})')

