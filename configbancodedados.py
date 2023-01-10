import sqlite3


con=sqlite3.connect('/shared/nossobancodedados.db')
cursor=con.cursor()
cursor.execute('create table if not exists Alunos(ra integer primary key, nome varchar(150))')
cursor.execute('create table if not exists Registro(ra integer, data varchar(20), estacao integer, acesso integer)')
con.commit()
with open('/shared/2022_2_eca10_alunos.csv', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha=linha.strip().split(';')
        cursor.execute(f"insert into Alunos values ({linha[0]}, '{linha[1]}');")
    con.commit()