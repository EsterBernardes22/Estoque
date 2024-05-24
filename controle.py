import pyodbc
from tkinter import *

dados_conexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost;Database=Estoque.db")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

def adicionar_insumo():
    cursor.execute('''
    INSERT INTO Estoque (Produto, Quantidade, DataValidade, Lote)
    VALUES (?, ?, ?, ?)
    ''', (nome_insumo.get(), qtde_insumo.get(), data_insumo.get(), lote_insumo.get()))
    conexao.commit()

    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"{nome_insumo.get()} Adicionado com sucesso")

def deletar_insumo():
    if len(nome_insumo.get()) > 2:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"Nome do insumo inválido")
        return   

    cursor.execute('''
        DELETE FROM Estoque
        WHERE Produto=?
    ''', (nome_insumo.get(),))
    conexao.commit()

    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"{nome_insumo.get()} Deletado com sucesso")

def registrar_uso_insumo():
    if len(nome_insumo.get()) < 2 or len(lote_insumo.get()) < 1 or len(qtde_insumo.get()) < 1:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"Nome, Lote, Quantidade de Insumo INVÁLIDOS")
        return
    cursor.execute('''
                   UPDATE Estoque
                   SET Quantidade=Quantidade-?
                   WHERE Produto=? AND Lote=?
                   ''', (qtde_insumo.get(), nome_insumo.get(), lote_insumo.get()))
    conexao.commit()

    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"{nome_insumo.get()} Foi consumido em {qtde_insumo.get()} unidades!!")


def procurar_insumo():
    nome = nome_insumo.get().strip()  
    if len(nome) < 2:  
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Nome do insumo inválido")
        return

    cursor.execute('''
        SELECT *
        FROM Estoque
        WHERE Produto=?
    ''', (nome_insumo.get(),))

    result = cursor.fetchone()

    if result:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", f"Insumo encontrado: {result}")
    else:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Insumo não encontrado")


window = Tk()

window.geometry("730x930")
window.configure(bg="#ffffff")

canvas = Canvas(
    window,
    bg="#ffffff",
    height=910,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="IMG/Textos.png")
background = canvas.create_image(374, 515, image=background_img)


img0 = PhotoImage(file= "IMG/BT01.png")
b0 = Button(
    image=img0, 
    borderwidth=0,
    highlightthickness=0,
    command=adicionar_insumo,  # Corrigido para chamar a função adicionar_insumo()
    relief="flat"
)

b0.place(
    x = 400, y = 330,
    width= 165,
    height=38
)

img1 = PhotoImage(file = "IMG/BT03.png")
b1 = Button(
    image = img1,
    borderwidth= 0,
    highlightthickness= 0,
    command= deletar_insumo,
    relief = "flat"
)

b1.place(
    x = 147, y = 331,
    width= 165,
    height=38
)


img2 = PhotoImage(file = "IMG/BT02.png")
b2 = Button(
    image = img2, 
    borderwidth= 0,
    highlightthickness= 0,
    command= registrar_uso_insumo, 
    relief = "flat"
)

b2.place(
    x = 400, y = 269,
    width= 165,
    height=38
)


img3 = PhotoImage(file= "IMG/BT04.png")
b3 = Button(
    image = img3, 
    borderwidth= 0,
    highlightthickness= 0,
    command= procurar_insumo,
    relief = "flat"
)

b3.place(
    x = 147, y = 272,
    width= 165,
    height=38
)


entry0_img = PhotoImage(file="IMG/Descrição.png")
entry0_bg = canvas.create_image(655, 860, image = entry0_img)

caixa_texto = Text(
    bd =0,
    bg= "#ffffff",
   highlightthickness= 0
)

caixa_texto.place(
    x = 168, y = 740,
   width= 430,
    height= 120
)

entry1_img = PhotoImage(file= "IMG/IMG04.png")
# Definir a imagem acima como Objeto e tela de fundo na tela
entry1_bg = canvas.create_image(425.0, 484.5, image = entry1_img)

nome_insumo = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness= 0
)
nome_insumo.place (
    x= 377, y= 423,
    width= 210,
    height=31
)

entry2_img = PhotoImage(file= "IMG/IMG03.png")
entry2_bg = canvas.create_image(425, 510.5, image = entry2_img)

data_insumo = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0
)

data_insumo.place (
    x= 377, y=500,
    width=210,
    height=31
)

entry3_img = PhotoImage(file= "IMG/IMG02.png")
entry3_bg = canvas.create_image(425.0, 540.5, image = entry3_img)

lote_insumo = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0
)

lote_insumo.place (
    x= 377, y=580,
    width=210,
    height=31
)

entry4_img = PhotoImage(file= "IMG/IMG01.png")
entry4_bg = canvas.create_image(425.0, 559.5, image = entry4_img)

qtde_insumo = Entry(
    bd=0,
    bg="#ffffff",
    highlightthickness=0
)

qtde_insumo.place (
    x= 377, y=650,
    width=210,
    height=31
)

window.resizable(False, False)
window.mainloop()
