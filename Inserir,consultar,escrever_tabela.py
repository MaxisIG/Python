import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import ttk
#from sqlite3 import *

def inicializaTabela():
    connessione = sqlite3.connect('BD_20221017.db')
    cursore = connessione.cursor()
    cursore.execute('DROP TABLE IF EXISTS Alunos;')
    cursore.execute('CREATE TABLE Alunos (rm INT PRIMARY KEY, nome VARCHAR(80), estado CHAR(2), nascimento DATE);')
    connessione.commit()
    connessione.close()

def insereDados(): #Método para inserir os dados da tabela .csv
    connessione = sqlite3.connect('BD_20221017.db')
    cursore = connessione.cursor()
    with open('tabela_alunos.csv', encoding='utf-8') as arquivo: #Acessa o arquivo csv
        for linha in arquivo:
            dados = linha.strip().replace("'",'').split(';')
            cursore.execute(f"INSERT INTO Alunos VALUES ({dados[0]},'{dados[1].strip()}','{dados[2].strip()}','{dados[3].strip()}');")
    connessione.commit()
    print(connessione.total_changes)
    connessione.close()

def digitarDados():
    connessione = sqlite3.connect('BD_20221017.db')
    cursore = connessione.cursor()
    rm = input('Digite o RM do aluno: ')
    nome = input('Digite o nome do aluno: ')
    estado = input('Digite o estado de residência do aluno [abreviado]: ')
    nascimento = input('Digite a data de nascimento do aluno [mm/dd/aaaa]: ')
    cursore.execute(f"INSERT INTO Alunos VALUES ({rm},'{nome.strip()}','{estado.strip()}','{nascimento.strip()}');")
    connessione.commit()
    connessione.close()

def consultaEstado(estado):
    connessione = sqlite3.connect('BD_20221017.db')
    cursore = connessione.cursor()
    cursore.execute(f"SELECT * FROM Alunos WHERE estado LIKE '{estado}';")
    resultado = cursore.fetchall()
    for registro in resultado:
        print(registro)
        
janela = tk.Tk()#Criando janela
#Configurando linhas e colunas
for x in range(3):
    janela.rowconfigure(x, weight = 1)#linhas
janela.columnconfigure(1, weight = 3)#colunas
janela.columnconfigure(2, weight = 2)#colunas
janela.title('Consulta de dados escolares')#colocando título na janela
#Criando e colocando informações em Label
textreset = ttk.Label(janela, text = 'Resetar a tabela')
textinserir = ttk.Label(janela, text= 'Inserir dados do excel para a tabela')
textnovo = ttk.Label(janela, text = 'Inserir novos dados para a tabela')
textconsulta = ttk.Entry(janela, textvariable = 'Escrever a sigla do Estado para consulta de dados na tabela')
#Criando Botões
buttonreset = ttk.Button(janela, text = 'Resetar tabela', command = inicializaTabela)
buttoninserir = ttk.Button(janela, text = 'Inserir dados Excel', command = insereDados)
buttonnovo = ttk.Button(janela, text = 'Novo dado', command = digitarDados)
buttonconsulta = ttk.Button(janela, text = 'Consultar dados', command = consultaEstado(textconsulta.get()))
#Mostrando as informações na janela
textreset.grid(row = 0, columnspan = 1, sticky = 'w')
textinserir.grid(row = 1, columnspan = 1, sticky = 'w')
textnovo.grid(row = 2, columnspan = 1, sticky = 'w')
buttonreset.grid(row = 0, columnspan = 2, sticky = 'e')
buttoninserir.grid(row = 1, columnspan = 2, sticky = 'e')
buttonnovo.grid(row = 2, columnspan = 2, sticky = 'e')
buttonconsulta.grid(row = 3, columnspan = 2, sticky = 'e')


janela.mainloop()