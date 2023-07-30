# Criando uma tupla
frutas = ('laranja', 'pera', 'uva')

letras = tuple('python')

numeros = tuple([1, 2, 3, 4])

pais = ('Brasil')

print(frutas)
print(letras)
print(numeros)
print(pais)

# Acessando os valores de uma tupla
print(frutas[0])
print(numeros[0])
print(letras[-1])

# Tuplas aninhadas
matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c')
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Iterar sobre uma tupla
for fruta in frutas:
    print(fruta)

# Iterar mostrando também o índice
for indice, fruta in enumerate(frutas):
    print(f'{indice}: {fruta}')
    
# MÉTODOS DE TUPLAS
# .count
cores = ('vermelho', 'azul', 'azul', 'verde')
print(cores.count('vermelho'))
print(cores.count('azul'))
print(cores.count('verde'))

print()
# .index
print(cores.index('verde'))

print()
# len
print(len(frutas)) # nesse caso, como a tupla possui dois elementos com mesmo valor, o python considera como apenas uma ocorrência
print(len(letras))


print()
carros = ('gol')
print(isinstance(carros, tuple))
