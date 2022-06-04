dividendo = int(input('Digite um número: '))
numero_digitado = dividendo
quociente = 1
lista = []
while quociente >= 1:
    resto = str(dividendo % 2)
    lista.append(resto)
    quociente = int(dividendo / 2)
    dividendo = quociente

resultado_final = reversed(lista)

print(f'Número da base decimal: {numero_digitado}')
print(f"Conversão para base binaria: {''.join(resultado_final)}")

