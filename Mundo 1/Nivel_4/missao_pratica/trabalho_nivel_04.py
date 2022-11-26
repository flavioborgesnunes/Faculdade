from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class Grafico:
  def __init__(self, lista_corridas):
    self.lista_corridas = lista_corridas
    self.imprimir_graficos()

  def padrao_do_grafico(self):
    plt.xlabel('Dia')
    plt.ylabel('Corrida em metros(m)')
    plt.title('Gráficos de Corridas')

  def imprimir_graficos(self):
    self.padrao_do_grafico()
    for corrida in self.lista_corridas:
      mLista = corrida.dicionario.items()
      cor = corrida.cor
      nome = corrida.nome
      x, y = zip(*mLista)
      plt.plot(x, y, label = nome, marker='o',
               markerfacecolor='blue',
               markersize=12,
               color=cor,
               linewidth=4)
    plt.legend()
    plt.show()

  def regressao_linear(self, id_grafico):
    corrida = self.lista_corridas[id_grafico]
    mLista = corrida.dicionario.items()
    cor = corrida.cor
    nome = corrida.nome
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


class Corrida:
    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor=cor
        self.nome = nome


maio = Corrida({1:1000,5:1000,7:1500,17:1500,20:1700,29:2000},'skyblue','maio')
junho = Corrida({1:1000,3:1000,5:1500,7:1500,15:1500,20:1700,27:2000},'red','junho')
julho = Corrida({1:1000,3:1000,5:1500,7:1500,10:2000,15:2000,20:2700,27:2500},'olive','julho')
lista_corridas = [maio,junho,julho]

grafico = Grafico(lista_corridas)