def dados():
    lista = []
    indice = 0
    conjunto = int(input('Defina o tamanho do conjunto: '))

    while len(lista) < conjunto:
        lista.append(int(input(f'Digite o item número {indice + 1}: ')))
        indice += 1

    return lista


def intermediarios(lista):
    lista2 = []
    combinacoes = [[]]

    for i in lista:
        lista2.append(i)
        combinacoes.append([i])

    for x in lista:
        for y in lista2:
            if lista2.index(y) >= lista.index(x) + 1:
                combinacoes.append([x, y])

    combinacoes.append(lista)

    return combinacoes


def apresentacao_dados():
    comibinacoes = intermediarios(dados())

    print(f'Essas são as combinações do conjuto: \n{comibinacoes}')


apresentacao_dados()
