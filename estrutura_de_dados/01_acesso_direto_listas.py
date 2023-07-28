# Acesso aos elementos de uma lista
frutas = ['maçã', 'laranja', 'uva', 'pera']

print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])

print()
# Listas aninhadas
matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

print()
# Fatiamento
lista = list('python')
print(lista)

print(lista[2:]) # ['t', 'h', 'o', 'n'] 
print(lista[:2]) # ['p', 'y']
print(lista[1:3]) # ['y', 't']
print(lista[0:3:2]) # ['p', 't']
print(lista[::]) # ['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1]) # ['n', 'o', 'h', 't', 'y', 'p']

print()
# Iterar sobre uma lista
carros = ['gol', 'celta', 'palio']
for carro in carros:
    print(carro)
    
print()

# função enumerate - às vezes é necessário saber qual o índice do objeto dentro do laço for
for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')
    
print()
'''List Comprehension - Compreensão de Listas -> oferece uma sintaxe mais curta quando você deseja gerar uma nova lista
com base nos valores de uma lista existente ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista 
existente.
'''
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []


# filtro versão 1
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

print()
# modificando valores da versão 1
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

print()
# filtro versão 2 - List comprehension
impares = [numero for numero in numeros if numero % 2 != 0]
print(impares)

print()
# modificando valores na versão 2 - list comprehension
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)