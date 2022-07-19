from cProfile import label
from cgitb import text
from operator import truediv
from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.fone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    def abrir(janela2):
        janela2 = tkinter.Toplevel()
        janela2.title('nova janela')

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()   
        self.frames_da_tela() 
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de clientes')
        self.root.configure(background= 'blue')
        self.root.geometry('750x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= '#dfe3ee',
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.3, relheight=0.95) 

        self.frame_2 = Frame(self.root, bd= 4, bg= '#dfe3ee',
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.35, rely=0.02, relwidth=0.6, relheight=0.95) 
   
        self.frame_3 = Frame(self.root, bd= 4, bg= '#dfe3ee',
                            highlightbackground='#759fe6', highlightthickness=3)
        self.frame_3.place(relx=0.35, rely=0.02, relwidth=0.6, relheight=0.95) 
    

    def widgets_frame1(self):

        #criando botões

        self.bt_cad_fe = Button(self.frame_1, text='Cadastrar', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'), command= self.abrir)
        self.bt_cad_fe.place(relx= 0.2, rely= 0.1, relwidth= 0.4, relheight= 0.07) 

        self.bt_cons_fe = Button(self.frame_1, text='Consultar', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'))
        self.bt_cons_fe.place(relx= 0.2, rely= 0.2, relwidth= 0.4, relheight= 0.07)

        self.bt_rem_fe = Button(self.frame_1, text='Remover', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'))
        self.bt_rem_fe.place(relx= 0.2, rely= 0.3, relwidth= 0.4, relheight= 0.07)

        self.bt_cad_tec = Button(self.frame_1, text='Cadastrar', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'))
        self.bt_cad_tec.place(relx= 0.2, rely= 0.6, relwidth= 0.4, relheight= 0.07)

        self.bt_cons_tec = Button(self.frame_1, text='Consultar', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'))
        self.bt_cons_tec.place(relx= 0.2, rely= 0.7, relwidth= 0.4, relheight= 0.07)

        self.bt_rem_tec = Button(self.frame_1, text='Remover', bd=3, bg='#107db2', fg="white"
                                                    , font=('verdana', 8, 'bold'))
        self.bt_rem_tec.place(relx= 0.2, rely= 0.8, relwidth= 0.4, relheight= 0.07)

        #criando label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = 'Ferramentas', bg= '#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx= 0.25, rely=0.00)

        # self.codigo_entry = Entry(self.frame_1)
        # self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        # #criando label e entrada do Nome
        self.lb_nome = Label(self.frame_1, text = 'Técnicos', bg= '#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx= 0.25, rely=0.5)

        # self.nome_entry = Entry(self.frame_1)
        # self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.8)

        # #criando label e entrada do telefone
        # self.lb_fone = Label(self.frame_1, text = 'Telefone', bg= '#dfe3ee', fg='#107db2')
        # self.lb_fone.place(relx= 0.05, rely=0.6)

        # self.fone_entry = Entry(self.frame_1)
        # self.fone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        # #criando label e entrada da cidade
        # self.lb_cidade = Label(self.frame_1, text = 'Cidade', bg= '#dfe3ee', fg='#107db2')
        # self.lb_cidade.place(relx= 0.5, rely=0.6)

        # self.cidade_entry = Entry(self.frame_1)
        # self.cidade_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns=('col1','col2','col3','col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0',width=1)
        self.listaCli.column('#1',width=50)
        self.listaCli.column('#2',width=200)
        self.listaCli.column('#3',width=125)
        self.listaCli.column('#4',width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll= self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


Application()