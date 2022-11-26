from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class Grafico:
  def __init__(self, lista_despesas):
    self.lista_despesas = lista_despesas
    self.imprimir_graficos()

  def padrao_do_grafico(self):
    plt.xlabel('Dia')
    plt.ylabel('Despesa em Reais(R$)')
    plt.title('Gráficos de despesas')

  def imprimir_graficos(self):
    self.padrao_do_grafico()
    for despesa in self.lista_despesas:
      mLista = despesa.dicionario.items()
      cor = despesa.cor
      nome = despesa.nome
      x, y = zip(*mLista)
      plt.plot(x, y, label = nome, marker='o',
               markerfacecolor='blue',
               markersize=12,
               color=cor,
               linewidth=4)
    plt.legend()
    plt.show()

  def regressao_linear(self, id_grafico):
    despesa = self.lista_despesas[id_grafico]
    mLista = despesa.dicionario.items()
    cor = despesa.cor
    nome = despesa.nome
    dias, valores = zip(*mLista)
    dias = np.array(dias)
    valores = np.array(valores)
    dias = dias.reshape(-1, 1)
    valores = valores.reshape(-1, 1)
    regr = LinearRegression()
    regr.fit(X=dias, y=valores)
    plt.plot(dias, regr.predict(dias),
             color='blue',
             label = "Regressão Linear")

    x, y = zip(*mLista)
    plt.plot(x, y, label = nome+str(" - original"),
             marker='o',
             markerfacecolor='olive',
             markersize=12,
             color=cor,
             linewidth=4)

    plt.legend()
    plt.show()


class despesa:
    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor=cor
        self.nome = nome


maio = despesa({1:259.50,5:600,7:159.75,17:1500,20:45.60,29:300},'skyblue','maio')
junho = despesa({1:259.50,3:750,5:124,7:750,15:300,20:159,27:150},'red','junho')
julho = despesa({1:269.50,3:750,5:412,7:600,10:350,15:84,20:130,27:300, 28:185.50},'olive','julho')
lista_despesas = [maio,junho,julho]

grafico = Grafico(lista_despesas)

id_mes = 1 
grafico.regressao_linear(id_mes)