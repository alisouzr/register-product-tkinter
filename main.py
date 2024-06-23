from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

import viewdb

janela = Tk()
janela.title('')
janela.geometry('700x490')
janela.configure(background="#e9edf5")
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam") 

# creating the frames for vizualization
frameUp = Frame(janela, width=1043, height=50, bg="#feffff", relief=FLAT)
frameUp.grid(row=0, column=0)

frameMid = Frame(janela, width=1043, height=190, bg="#feffff", relief=FLAT)
frameMid.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBottom = Frame(janela, width=1043, height=300, bg="#feffff", relief=FLAT)
frameBottom.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# criando funções
global tree
# Função inserir
def insert():
    name = e_name.get()
    description = e_description.get()
    value = e_value.get()

    try:
        value = float(value)
        
        if e_available.get() == 1:
            available = 'sim'
        else:
            available = 'não'

        list_insert = [name, description, value, available]

        for data in list_insert:
            if data == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        viewdb.insert_data(list_insert)

        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_name.delete(0, 'end')
        e_description.delete(0, 'end')
        e_value.delete(0, 'end')

        show_data_in_bottom()
    except:
        messagebox.showerror('Erro', 'Insira um número float no campo valor')

    

def atualizar():
    e_name.delete(0, 'end')
    e_description.delete(0, 'end')
    e_value.delete(0, 'end')
    
    try:
        global tree

        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        id = int(treev_lista[0])
        e_name.insert(0, treev_lista[1])
        e_description.insert(0, treev_lista[2])
        e_value.insert(0, treev_lista[3])

        def update():
            
            name = e_name.get()
            description = e_description.get()
            value = e_value.get()

            try:
                value = float(value)

                if e_available.get() == 1:
                    available = 'sim'
                else:
                    available = 'não'

                list_update = [name, description, value, available, id]

                for data in list_update:
                    if data == '':
                        messagebox.showerror('Erro', 'Preencha todos os campos.')
                        return
                    
                viewdb.update_data(list_update)

                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso.')

                e_name.delete(0, 'end')
                e_description.delete(0, 'end')
                e_value.delete(0, 'end')

                b_confirm.destroy()

                show_data_in_bottom()
            except:
                messagebox.showerror('Erro', 'Insira um número float no campo valor')

        b_confirm = Button(frameMid, command=update,text='Confirmar'.upper(), overrelief=RIDGE, font='Ivy, 10 bold', bg='#4fa882', fg='#feffff')
        b_confirm.place(x=330, y=150)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def delete():
    try:
        global tree

        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0]

        viewdb.delete_data([valor])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso.')

        show_data_in_bottom()

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')



app_title = Label(frameUp, text='Cadastro Produto', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg="#feffff", fg="#403d3d")
app_title.place(x=0, y=0)

# creating entrys
l_name = Label(frameMid, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d')
l_name.place(x=10, y=10)
e_name = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_name.place(x=130, y=11)

l_description = Label(frameMid, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d')
l_description.place(x=10, y=40)
e_description = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_description.place(x=130, y=41)

l_value = Label(frameMid, text='Valor', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d')
l_value.place(x=10, y=70)
e_value = Entry(frameMid, width=30, justify='left', relief=SOLID)
e_value.place(x=130, y=71)

l_available = Label(frameMid, text='Disponível', height=1, anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d')
l_available.place(x=10, y=100)

e_available = IntVar()

rad1 = Radiobutton(frameMid,text='sim', value=1, variable=e_available)
rad1.place(x=130, y=100)

rad2 = Radiobutton(frameMid,text='não', value=2, variable=e_available)
rad2.place(x=180, y=100)


b_insert = Button(frameMid, command=insert, text='Adicionar'.upper(), compound=CENTER, anchor=NW, overrelief=RIDGE, font='Ivy, 10 bold', bg='#feffff', fg='#403d3d')
b_insert.place(x=330, y=10)

b_update = Button(frameMid, command=atualizar,text='Atualizar'.upper(), compound=CENTER, anchor=NW, overrelief=RIDGE, font='Ivy, 10 bold', bg='#feffff', fg='#403d3d')
b_update.place(x=330, y=50)

b_delete = Button(frameMid, command=delete,text='Deletar'.upper(), compound=CENTER, anchor=NW, overrelief=RIDGE, font='Ivy, 10 bold', bg='#feffff', fg='#403d3d')
b_delete.place(x=330, y=90)

l_total = Label(frameMid, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg='#3fbfb9', fg='#feffff')
l_total.place(x=450, y=17)
l_total_ = Label(frameMid, text='  Valor total de todos os itens   ',height=1, anchor=NW, font=('Ivy 10 bold'), bg="#3fbfb9", fg='#feffff')
l_total_.place(x=450, y=12)

l_qtd = Label(frameMid, text='', width=14, height=2, pady=5,anchor=CENTER, font=('Ivy 17 bold'), bg='#3fbfb9', fg='#feffff')
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameMid, text='  Valor total de todos os itens   ',height=1, anchor=NW, font=('Ivy 10 bold'), bg='#3fbfb9', fg='#feffff')
l_qtd_.place(x=450, y=92)

def show_data_in_bottom():
    ##################################
    table_head = ['#Item','Nome',  'Descrição', 'Valor da compra', 'Disponível']

    list_itens = viewdb.view_data()

    global tree

    tree = ttk.Treeview(frameBottom, selectmode="extended",columns=table_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBottom, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBottom, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBottom.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center"]
    h=[40,150,200,160,130]
    n=0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    # inserindo os itens dentro da tabela
    for item in list_itens:
        tree.insert('', 'end', values=item)


    quantity = []

    for iten in list_itens:
        quantity.append(iten[3])



    total_amount = sum(quantity)
    total_itens = len(quantity)

    l_total['text'] = 'R$ {:,.2f}'.format(total_amount)
    l_qtd['text'] = total_itens

show_data_in_bottom()

janela.mainloop()