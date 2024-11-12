import sqlite3

# Função que conecta o banco de dados

def conectar_banco ():
    conexao = sqlite3.connect('meu_banco.db')
    cursor = conexao.cursor()

    #parte principal do programa
    if__name__=='__main__':
    conectar_banco