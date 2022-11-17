#1o. passo: importar a biblioteca sqlite3
import sqlite3

#Passos 2 e 3 virarão função conectar()
def conectar():

  #2o. passo: Vamos estabelecer uma 
  #conexão com o banco de dados

  conexao = sqlite3.connect("dc_universe.db")

  #3o. passo: criar um objeto do tipo cursor
  cursor = conexao.cursor()

  return conexao, cursor