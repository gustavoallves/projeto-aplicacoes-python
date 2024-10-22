import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter import PhotoImage
import re
import sqlite3

#começar com tela com um botão e um entry (nome)- v1
#adicionar mais duas entrys (cpf e estado) e suas labels - v2
#mudar o fundo para uma imagem mais bonita, adicionar readme.txt explicando como usar - v3
#adicionar clicar no botão salva os 3 dados em um sqlite - v4
#Criar uma branch em que le um config.txt com uma lista de 5 estados possiveis separados por pular linha - x1
#Mudar o separador para ; e adicionar mais 5 estados - x2
#Voltar para main, criar outra branch e criar um dropdown com 3 opções (clt, mei, socio) - y1
#Voltar para main, Corrigir o bug da função de cpf - v5
#Merge de x com v - v6
#Adicionar verificação de CPF e de estado, com base na função cpf e na lista de estados .txt antes de adicionar no sqlite v7

#Cria conexão
connection = sqlite3.connect("Pessoa.db")

#Cria o cursos e cria a tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Tabela1 (nome TEXT, cpf INTEGER, estado TEXT)")
def verificarCPF(cpf):
    padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    if re.match(padrao_cpf, cpf):
        return True
    else:
        return False

def salvar_dados(nome, cpf, estado):
    if verificarCPF(cpf):
        cursor.execute("INSERT INTO Tabela1 (nome, cpf, estado) VALUES (?, ?, ?)", (nome, cpf, estado))
        connection.commit()
        print(f"Dados salvos: Nome: {nome}, CPF: {cpf}, Estado: {estado}")
        e1.delete(0, tkinter.END)
        e2.delete(0, tkinter.END)
        e3.delete(0, tkinter.END) 

    else:
        print("CPF inválido! Deve estar no formato 000.000.000-00")


def criar_readme():
    readme_txt = """
    Instruções de Uso:
    
    1. Insira o nome no campo 'Nome'.
    2. Insira o CPF no formato 000.000.000-00.
    3. Insira o estado.
    4. Clique no botão 'Salvar' para capturar e salvar os dados.
    """
    with open("README.txt", "w") as readme_file:
        readme_file.write(readme_txt)

def inserevalores(nome, cpf=0, estado="Estado"):
    #Insere linha na tabela
    cursor.execute("INSERT INTO Tabela1 VALUES ('"+nome+"', '"+cpf+"', '"+estado+"')")

def pegavalores():
    #Pega valores da tabela
    rows = cursor.execute("SELECT * FROM Tabela1").fetchall()
    print(rows)

def funcExemplo():
    print("Exemplo de funcao")
    
def Main():
    global e1
    global e2
    global e3
    root = tkinter.Tk()
    root.geometry('300x300')
    root.title("Projeto Nome-CPF-Estado")

    root.title("Trabalho RAD")
    root.resizable(False, False)
    
    try:
        bg_image = PhotoImage(file="bg-ceu.png")
        background_label = tkinter.Label(root, image=bg_image)
        background_label.place(relwidth=1, relheight=1)
    except:
        print("Imagem de fundo não encontrada.")

    label = tkinter.Label(root, text="Nome")
    label.pack()

    text_nome = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:text_nome.set(e1.get()+x.char))
    e1.pack()

    label_cpf = tkinter.Label(root, text="CPF")
    label_cpf.pack()

    text_cpf = tkinter.StringVar()
    e2 = tkinter.Entry(root, textvariable=text_cpf)
    e2.pack()

    label_estado = tkinter.Label(root, text="Estado")
    label_estado.pack()

    text_estado = tkinter.StringVar()
    e3 = tkinter.Entry(root, textvariable=text_estado)
    e3.pack()

    salvar_btn = tkinter.Button(root, text="Salvar", command=lambda: salvar_dados(text_nome.get(), text_cpf.get(), text_estado.get()))

    salvar_btn.pack()

    root.iconify() #Minimiza a tela
    root.update()
    root.deiconify() #Maximiza a tela
    root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
    criar_readme()

if __name__ == "__main__":
    Main()
