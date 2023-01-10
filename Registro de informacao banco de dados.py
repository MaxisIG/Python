import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime
from tkinter import messagebox

#Atenção com o caminho dos arquivos----------------------------------------------------------

def CriarTabela():
    res = messagebox.askyesno("Novas Tabelas", "Certeza que quer criar um nova tabela, todos os registros serão apagados")
    if res:
        conexaoBD = sqlite3.connect("D:/FTT/2022.2/Python/eca10_2022_2.db")
        cursor = conexaoBD.cursor()
        cursor.execute("DROP TABLE IF EXISTS venda;")
        cursor.execute("DROP TABLE IF EXISTS produto;")
        cursor.execute("DROP TABLE IF EXISTS cliente;")
        cursor.execute("CREATE TABLE  IF NOT EXISTS produto ( cod_prod INTEGER PRIMARY KEY AUTOINCREMENT,descricao VARCHAR[80] NOT NULL,valor_unit DECIMAL(10, 2));")
        cursor.execute("CREATE TABLE IF NOT EXISTS cliente (cod_cli INTEGER PRIMARY KEY AUTOINCREMENT,CNPJ VARCHAR[14],nome_fant VARCHAR[80]);")
        cursor.execute("CREATE TABLE venda (cod_venda INTEGER PRIMARY KEY AUTOINCREMENT,data VARCHAR[40],cod_prod INT FOREING KEY REFERENCES produto(cod_prod),cod_cli INT FOREING KEY REFERENCES cliente(cod_cli),qtdade INT);")
        conexaoBD.close()

def buscaLista(campo, tabela, condicao = None):
    conexaoBD = sqlite3.connect("D:/FTT/2022.2/Python/eca10_2022_2.db")
    cursor = conexaoBD.cursor()
    try:
        if condicao == None:
            cursor.execute(f'SELECT {campo} FROM {tabela};')
            resultado = cursor.fetchall()
            print(resultado)
            conexaoBD.close()
            return resultado
        else:
            cursor.execute(f'SELECT {campo} FROM {tabela} WHERE {condicao};')
            resultado = cursor.fetchall()
            conexaoBD.close()
            return resultado

    except:
        conexaoBD.close()
        return False

def executaSQL(instrucao):
    print(instrucao)
    conexaoBD = sqlite3.connect("D:/FTT/2022.2/Python/eca10_2022_2.db")
    cursor = conexaoBD.cursor()
    try:
        cursor.execute(instrucao)
        conexaoBD.commit()
        conexaoBD.close()
    except:
        conexaoBD.close()
        return False
    return True

def registraProduto():
    resp = executaSQL(f"INSERT INTO produto (descricao, valor_unit) VALUES ('{ent_ProdDesc.get()}',{ent_ProdValor.get().replace(',','.')});")
    if resp:
        print("Uau, funcionou")
    else:
        print("Deu ruim...")

def registraCliente():
    resp = executaSQL(f"INSERT INTO cliente (CNPJ, nome_fant) VALUES ('{ent_CliCNPJ.get()}','{ent_CliNome.get()}');")
    if resp:
        print("Uau, funcionou")
    else:
        print("Deu ruim...")

def registraVenda():
    codProd = buscaLista('cod_prod', 'produto', f'descricao = {cbb_VendaProd.get()}')
    codCli = buscaLista('cod_cli', 'cliente', f'nome_fant = {cbb_VendaCli.get()}')
    x = datetime.datetime.now()
    y = x.strftime("%x")
    resp = executaSQL(f"INSERT INTO venda (data, cod_prod, cod_cli, qtdade) VALUES ('{y}','{cbb_VendaProd.get()}','{cbb_VendaCli.get()}','{ent_Qtd.get()}');")
    if resp:
        print("Uau, funcionou")
    else:
        print("Deu ruim...")
    #Instruções para iniserir o registro na tabela de vendas
def VerTabelaVenda():
    buscaLista("*", "venda")
    
def VerTabelaProduto():
    buscaLista("*", "produto")
    
def VerTabelaCliente():
    buscaLista("*", "cliente")
    


ventana = tk.Tk()
ventana.geometry("300x600")

#Ferramentas
frm_Registro = ttk.LabelFrame(ventana, text = "Criar Tabela", relief = 'sunken')
frm_Produto = ttk.LabelFrame(ventana, text = "Produto", relief = 'sunken')
frm_Cliente = ttk.LabelFrame(ventana, text = "Cliente", relief = 'sunken')
frm_Venda = ttk.LabelFrame(ventana, text = "Venda", relief = 'sunken')
lbl_Registro = ttk.Label(frm_Registro, text = "Cuidado ao clicar em Criar Tabela \n Todos os registros serão perdidos \n Será criado uma tabela sem nenhum registro")
lbl_ProdDesc = ttk.Label(frm_Produto, text="Descrição")
lbl_ProdValor = ttk.Label(frm_Produto, text="Valor [R$]")
lbl_Qtd = ttk.Label(frm_Venda, text = "Quantidade")
lbl_CliNome = ttk.Label(frm_Cliente, text="Nome fantasia")
lbl_CliCNPJ = ttk.Label(frm_Cliente, text="CNPJ")
lbl_VendaProd = ttk.Label(frm_Venda, text="Descrição do produto")
lbl_VendaCli = ttk.Label(frm_Venda, text="Cliente")
ent_ProdDesc = ttk.Entry(frm_Produto)
ent_ProdValor = ttk.Entry(frm_Produto)
ent_Qtd = ttk.Entry(frm_Venda)
ent_CliNome = ttk.Entry(frm_Cliente)
ent_CliCNPJ = ttk.Entry(frm_Cliente)
btn_RegistrarTabela = ttk.Button(frm_Registro, text = "Criar Tabela", command = CriarTabela)
btn_NovoProd = ttk.Button(frm_Produto, text="Registrar produto", command=registraProduto)
btn_NovoCli = ttk.Button(frm_Cliente, text="Registrar cliente", command=registraCliente)
btn_NovaVenda = ttk.Button(frm_Venda, text="Registrar venda", command = registraVenda)
btn_VerVenda = ttk.Button(frm_Registro, text = "Exibir Tabela de Venda", command = VerTabelaVenda)
btn_VerProduto = ttk.Button(frm_Registro, text = "Exibir Tabela de Produto", command = VerTabelaProduto)
btn_VerCliente = ttk.Button(frm_Registro, text = "Exibir Tabela de Cliente", command = VerTabelaCliente)
cbb_VendaProd = ttk.Combobox(frm_Venda)
cbb_VendaProd['values'] = buscaLista('descricao','produto')
cbb_VendaCli = ttk.Combobox(frm_Venda)
cbb_VendaCli['values'] = buscaLista('nome_fant','cliente')

#Montagem da interface
ventana.rowconfigure([0,1,2,3], weight = 1)
ventana.columnconfigure(0, weight = 1)

frm_Registro.grid(row = 0, column = 0, sticky = 'news')
frm_Produto.grid(row=1,column=0, sticky = "news")
frm_Cliente.grid(row=2,column=0, sticky = "news")
frm_Venda.grid(row=3,column=0, sticky = "news")

btn_RegistrarTabela.grid(row = 0, column = 0, )
lbl_Registro.grid(row = 0, column = 1)
btn_VerVenda.grid(row = 3, column = 0)
btn_VerProduto.grid(row = 3, column = 1)
btn_VerCliente.grid(row = 3, column = 2)



lbl_ProdDesc.grid(row=0,column=0)
ent_ProdDesc.grid(row=0, column=1)
lbl_ProdValor.grid(row=1,column=0)
ent_ProdValor.grid(row=1, column=1)
btn_NovoProd.grid(row=0, column=2, rowspan=2)


lbl_CliNome.grid(row=0,column=0)
ent_CliNome.grid(row=0, column=1)
lbl_CliCNPJ.grid(row=1,column=0)
ent_CliCNPJ.grid(row=1, column=1)
btn_NovoCli.grid(row=0, column=2, rowspan=2)

lbl_VendaCli.grid(row=0,column=0)
cbb_VendaCli.grid(row=0, column=1)
lbl_VendaProd.grid(row=1,column=0)
cbb_VendaProd.grid(row=1, column=1)
btn_NovaVenda.grid(row=0, column=2, rowspan=2)
lbl_Qtd.grid(row = 3, column = 0)
ent_Qtd.grid(row = 3, column = 1)

ventana.mainloop()