from objetos import *
import string
# from numpy import unicode_
# from pyparsing import unicode_string
# from ferramentas import ferramentas 
# from openpyxl import Workbook, load_workbook
import unicodedata




idd = 1
des = str(input('Descrição: ')).capitalize().strip()
fb = str(input('Fabricante: ')).capitalize().strip()
vts = float(input('Voltagem: '))
num = int(input('Número de fabricação: '))
tam = str(input('Medida da ferramenta: ')).capitalize().strip()
med = str(input('Unidade de medida: ')).capitalize().strip()
tip = str(input('Tipo da ferramenta: ')).capitalize().strip()
mat = str(input('Tipo de material da ferramenta: ')).capitalize().strip()
temp = float(input('Tempo máximo de reserva: hrs'))

ferramenta = ferramentas(idd, des, fb, vts, num, tam, med, tip, mat, temp)

#----------------------------------------------

wb = Workbook()

# wb = load_workbook('Trabalho_Faculdade\Missão_certificação\ ferramentas.xlsx')
ws = wb.active
ws.title = 'Ferramentas'

ws.append([ferramenta.Id_ferramentas,ferramenta.descricao, ferramenta.fabricante, ferramenta.volts, ferramenta.number, ferramenta.tamanho, ferramenta.medida, ferramenta.tipo, ferramenta.material, ferramenta.tempo])
wb.save('Trabalho_Faculdade\Missão_certificação\ ferramentas.xlsx')
print('Salvo com sucesso!')
