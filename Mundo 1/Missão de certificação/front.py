from cProfile import label
from logging import root
from this import s
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
# from funcao import criarFerramenta

from setuptools import Command


root = Tk()


class Application():
    fontStyle = tkFont.Font(family="Lucida Grande", size=7)
    # acão do botão cadastro

    def botao_cadastroF(self):
        # print('cadastro')
        self.frame_cadastro = Frame(
            self.root, bd=4, bg='#FF00FF', highlightbackground='#aabbcc', highlightthickness=0)
        self.frame_cadastro.place(
            relx=0.23, rely=0.0, relwidth=0.77, relheight=1)
        self.frame_cadastro

        self.lb_descricao = Label(self.frame_cadastro, text='Descrição da Ferramenta',
                                  bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_descricao.place(relx=0.05, rely=0.02)
        self.descricao_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.descricao_entry.place(
            relx=0.05, rely=0.07, relwidth=0.60, relheight=0.04)
        self.lb_fabricante = Label(
            self.frame_cadastro, text='Fabricante', bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_fabricante.place(relx=0.05, rely=0.12)
        self.fabricante_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.fabricante_entry.place(
            relx=0.05, rely=0.17, relwidth=0.60, relheight=0.04)
        self.lb_voltagem = Label(self.frame_cadastro, text='Voltagem',
                                 bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_voltagem.place(relx=0.05, rely=0.22)
        self.voltagem_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.voltagem_entry.place(
            relx=0.05, rely=0.27, relwidth=0.60, relheight=0.04)
        self.lb_partnumber = Label(
            self.frame_cadastro, text='Part Number', bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_partnumber.place(relx=0.05, rely=0.32)
        self.partnumber_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.partnumber_entry.place(
            relx=0.05, rely=0.37, relwidth=0.60, relheight=0.04)
        self.lb_tamanho = Label(self.frame_cadastro, text='Tamanho',
                                bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_tamanho.place(relx=0.05, rely=0.42)
        self.tamanho_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.tamanho_entry.place(relx=0.05, rely=0.47,
                                 relwidth=0.60, relheight=0.04)
        self.lb_unidade = Label(self.frame_cadastro, text='Unidade de Medida',
                                bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_unidade.place(relx=0.05, rely=0.52)
        self.unidade_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.unidade_entry.place(relx=0.05, rely=0.57,
                                 relwidth=0.60, relheight=0.04)
        self.lb_tipo = Label(self.frame_cadastro, text='Tipo da Ferramenta',
                             bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_tipo.place(relx=0.05, rely=0.62)
        self.tipo_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.tipo_entry.place(relx=0.05, rely=0.67,
                              relwidth=0.60, relheight=0.04)
        self.lb_material = Label(self.frame_cadastro, text='Material da Ferramenta',
                                 bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_material.place(relx=0.05, rely=0.72)
        self.material_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.material_entry.place(
            relx=0.05, rely=0.77, relwidth=0.60, relheight=0.04)
        self.lb_tempo = Label(self.frame_cadastro, text='Tempo Máximo de Reserva',
                              bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_tempo.place(relx=0.05, rely=0.82)
        self.tempo_entry = Entry(
            self.frame_cadastro, highlightbackground='#878787', highlightthickness=1)
        self.tempo_entry.place(relx=0.05, rely=0.87,
                               relwidth=0.60, relheight=0.04)

        self.bt_cadastrarF = Button(
            self.frame_cadastro, text='Cadastrar', bg='#F2F2F2')
        self.bt_cadastrarF.place(
            relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)

    def botao_cadastroTec(self):
        # print('c')
        self.frame_cadastroTec = Frame(
            self.root, bd=4, bg='red', highlightbackground='#aabbcc', highlightthickness=0)
        self.frame_cadastroTec.place(
            relx=0.23, rely=0.0, relwidth=0.77, relheight=1)
        self.frame_cadastroTec

        self.lb_cpf = Label(self.frame_cadastroTec, text='CPF',
                            bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_cpf.place(relx=0.05, rely=0.02)
        self.cpf_entry = Entry(
            self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
        self.cpf_entry.place(relx=0.05, rely=0.07,
                             relwidth=0.60, relheight=0.04)
        self.lb_nome = Label(self.frame_cadastroTec, text='Nome',
                             bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_nome.place(relx=0.05, rely=0.12)
        self.nome_entry = Entry(
            self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
        self.nome_entry.place(relx=0.05, rely=0.17,
                              relwidth=0.60, relheight=0.04)
        self.lb_Telefone = Label(self.frame_cadastroTec, text='Telefone',
                                 bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_Telefone.place(relx=0.05, rely=0.22)
        self.Telefone_entry = Entry(
            self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
        self.Telefone_entry.place(
            relx=0.05, rely=0.27, relwidth=0.60, relheight=0.04)
        self.lb_turno = Label(self.frame_cadastroTec, text='Turno',
                              bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_turno.place(relx=0.05, rely=0.32)
        self.turno_entry = Entry(
            self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
        self.turno_entry.place(relx=0.05, rely=0.37,
                               relwidth=0.60, relheight=0.04)
        self.lb_equipe = Label(self.frame_cadastroTec, text='Nome da Equipe',
                               bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_equipe.place(relx=0.05, rely=0.42)
        self.equipe_entry = Entry(
            self.frame_cadastroTec, highlightbackground='#878787', highlightthickness=1)
        self.equipe_entry.place(relx=0.05, rely=0.47,
                                relwidth=0.60, relheight=0.04)

        self.bt_cadastrarF = Button(
            self.frame_cadastroTec, text='Cadastrar', bg='#F2F2F2')
        self.bt_cadastrarF.place(
            relx=0.7, rely=0.6, relwidth=0.3, relheight=0.05)

    def botao_consultaF(self):
        # print('consulta')
        self.frame_consultaFer = Frame(
            self.root, bd=4, bg='blue', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaFer.place(
            relx=0.23, rely=0.0, relwidth=0.77, relheight=1)
        self.frame_consultaFer

        self.lb_codigo = Label(self.frame_consultaFer, text='Código',
                               bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_codigo.place(relx=0.05, rely=0.02)
        self.codigo_entry = Entry(
            self.frame_consultaFer, highlightbackground='#878787', highlightthickness=1)
        self.codigo_entry.place(relx=0.05, rely=0.07,
                                relwidth=0.60, relheight=0.04)

        self.listaCli = ttk.Treeview(self.frame_consultaFer, height=1, columns=(
            'col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Desc')
        self.listaCli.heading('#3', text='Fab')
        self.listaCli.heading('#4', text='volt')
        self.listaCli.heading('#5', text='P.Num')
        self.listaCli.heading('#6', text='Tam')
        self.listaCli.heading('#7', text='U.Med')
        self.listaCli.heading('#8', text='Tipo')
        self.listaCli.heading('#9', text='Material')
        self.listaCli.heading('#10', text='Res')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=50)
        self.listaCli.column('#3', width=50)
        self.listaCli.column('#4', width=50)
        self.listaCli.column('#5', width=50)
        self.listaCli.column('#6', width=50)
        self.listaCli.column('#7', width=50)
        self.listaCli.column('#8', width=50)
        self.listaCli.column('#9', width=50)
        self.listaCli.column('#10', width=50)

        self.listaCli.place(relx=0.01, rely=0.3, relwidth=0.95, relheight=0.5)

        self.scrollLista = Scrollbar(self.frame_consultaFer, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.3,
                               relwidth=0.04, relheight=0.5)

        self.bt_excluirF = Button(
            self.frame_consultaFer, text='Excluir', bg='#F2F2F2')
        self.bt_excluirF.place(
            relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)
        self.bt_funcaoFer = Button(
            self.frame_consultaFer, text='Consultar', bg='#F2F2F2')
        self.bt_funcaoFer.place(
            relx=0.3, rely=0.9, relwidth=0.3, relheight=0.05)

    def botao_consultaTec(self):
        # print('consulta Tec')
        self.frame_consultaTec = Frame(
            self.root, bd=4, bg='green', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaTec.place(
            relx=0.23, rely=0.0, relwidth=0.77, relheight=1)
        self.frame_consultaTec

        self.lb_codigo = Label(self.frame_consultaTec, text='CPF',
                               bg='#FFFFFF', foreground='black', font='fontStyle')
        self.lb_codigo.place(relx=0.05, rely=0.02)
        self.codigo_entry = Entry(
            self.frame_consultaTec, highlightbackground='#878787', highlightthickness=1)
        self.codigo_entry.place(relx=0.05, rely=0.07,
                                relwidth=0.60, relheight=0.04)

        self.listaCli = ttk.Treeview(self.frame_consultaTec, height=1, columns=(
            'col1', 'col2', 'col3', 'col4', 'col5'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='CPF')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Turno')
        self.listaCli.heading('#5', text='Equipe')

        self.listaCli.column('#0', width=0)
        self.listaCli.column('#1', width=100)
        self.listaCli.column('#2', width=100)
        self.listaCli.column('#3', width=100)
        self.listaCli.column('#4', width=100)
        self.listaCli.column('#5', width=100)

        self.listaCli.place(relx=0.01, rely=0.3, relwidth=0.95, relheight=0.5)

        self.scrollLista = Scrollbar(self.frame_consultaTec, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.3,
                               relwidth=0.04, relheight=0.5)

        self.bt_excluirTec = Button(
            self.frame_consultaTec, text='Excluir', bg='#F2F2F2')
        self.bt_excluirTec.place(
            relx=0.7, rely=0.9, relwidth=0.3, relheight=0.05)
        self.bt_funcaoFer = Button(
            self.frame_consultaTec, text='Consultar', bg='#F2F2F2')
        self.bt_funcaoFer.place(
            relx=0.3, rely=0.9, relwidth=0.3, relheight=0.05)

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets_frame1()
        self.botao_consultaF()
        self.botao_cadastroTec()
        self.botao_consultaTec()
        self.botao_cadastroF()
        root.mainloop()

    def tela(self):
        self.root.title('Central de Ferramentaria')
        self.root.configure(background='#463A3E')
        self.root.geometry('900x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=420)

    def frames_de_tela(self):

        self.frame_2 = Frame(self.root, bd=4, bg='gray',
                             highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_2.place(relx=0, rely=0.0, relwidth=0.23, relheight=1)

        self.frame_cadastroTec = Frame(
            self.root, bd=4, bg='red', highlightbackground='#878787', highlightthickness=0.5)
        self.frame_cadastroTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_cadastro = Frame(
            self.root, bd=4, bg='yellow', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_cadastro.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_consultaFer = Frame(
            self.root, bd=4, bg='red', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaFer.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

        self.frame_consultaTec = Frame(
            self.root, bd=4, bg='green', highlightbackground='#0D0D0D', highlightthickness=0)
        self.frame_consultaTec.place(
            relx=0.23, rely=0.00, relwidth=0.77, relheight=1)

    def widgets_frame1(self):
        # Botão cadastar ferramentas
        self.bt_cadastroFer = Button(
            self.frame_2, text=' Ferramentas', bg='#F2F2F2', command=self.botao_cadastroF)
        self.bt_cadastroFer.place(
            relx=0.01, rely=0.1, relwidth=1, relheight=0.05)
        # Botão cadastrar tecnico
        self.bt_cadastroTec = Button(
            self.frame_2, text='Técnicos', bg='#F2F2F2', command=self.botao_cadastroTec)
        self.bt_cadastroTec.place(
            relx=0.01, rely=0.152, relwidth=1, relheight=0.05)
        # Botão consulta Ferramenta
        self.bt_consultaFer = Button(
            self.frame_2, text='Ferramentas', bg='#F2F2F2', command=self.botao_consultaF)
        self.bt_consultaFer.place(
            relx=0.01, rely=0.30, relwidth=1, relheight=0.05)
        # Botão consultar Técnico
        self.bt_consultaTec = Button(
            self.frame_2, text='Técnicos', bg='#F2F2F2', command=self.botao_consultaTec)
        self.bt_consultaTec.place(
            relx=0.01, rely=0.353, relwidth=1, relheight=0.05)
        # texto cadastro
        self.lb_cadastro = Label(
            self.frame_2, text='Cadastro', bg='#130633', foreground='white', font='fontStyle')
        self.lb_cadastro.place(relx=0.01, rely=0.05,
                               relwidth=1, relheight=0.05)
        # texto consulta
        self.lb_consulta = Label(
            self.frame_2, text='Consulta', bg='#130633', foreground='white', font='fontStyle')
        self.lb_consulta.place(relx=0.01, rely=0.25,
                               relwidth=1, relheight=0.05)


Application()
