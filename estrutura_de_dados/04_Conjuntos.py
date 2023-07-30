# Declarando conjuntos
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)
letras = set('abacaxi')
print(letras)
carros = {'palio', 'gol', 'celta', 'palio'}
print(carros)
linguagens = {'python', 'java', 'js', 'java'}
print(linguagens)

print()
# Acessando os dados de um conjunto
numeros = list(numeros)
print(numeros[0])

print()
# Iterar conjuntos
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')    
print()

# MÉTODOS DA CLASSE SET
# .union
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.union(conjunto_b))
conjuntos_unidos = conjunto_a.union(conjunto_b)
print(conjuntos_unidos)

print()
# intersection()
print(conjunto_a.intersection(conjunto_b))

print()
# difference()
print(conjunto_a.difference(conjunto_b)) # aqui mostra o que tem no conjunto a, mas não existe no b
print(conjunto_b.difference(conjunto_a)) # aqui mostra o que tem no conjunto b, mas que não existe no a

print()
# symmetric_diffeerence()
print(conjunto_a.symmetric_difference(conjunto_b)) # aqui mostra os elementos diferentes dos dois sets, de uma vez só

print()
# issubset()
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5, 6}

print(conjunto_a.issubset(conjunto_b)) # verifica se o conjunto a está presente dentro do conjunto b
print(conjunto_b.issubset(conjunto_a)) # verifica se conjunto b está presente dentro do conjunto a

print()
# issuperset()
print(conjunto_a.issuperset(conjunto_b)) # verifica se o conjunto a possui o conjunto b dentro de si
print(conjunto_b.issuperset(conjunto_a)) # verifica se o conjunto b possui o conjunto a dentro de si

print()
# isdisjoint()
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b)) # verifica se o conjunto a não coincide com o conjunto b em nenhum elemento
print(conjunto_a.isdisjoint(conjunto_c)) # verifica se o conjunto a não coincide com o conjunto c em nenhum elemento

print()
# add()
conjunto_c.add(4) # adiciona o elemento 4 ao conjunto c
conjunto_c.add(3) # adiciona o elemento 3 ao conjunto c
print(conjunto_c)
conjunto_c.add(3) # adiciona o elemento 3 ao conjunto c, porém esse elelmento já existe, então será ignorado
print(conjunto_c)

print()
# clear()
conjunto_c.clear() # limpa o set
print(conjunto_c)

print()
# copy()
conjunto_c = conjunto_a.copy()
print(conjunto_c) # copia um conjunto, nesse caso copia o conjunto a e o atribui ao conjunto c

print()
# discard()
conjunto_c.discard(2) # descartou o valor 2 do conjunto c
print(conjunto_c)

print()
# pop()
conjunto_d = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(conjunto_d)
print(conjunto_d.pop())
print(conjunto_d.pop())
print(conjunto_d.pop())
print(conjunto_d)

print()
# remove() - se eu pedir para remover um elemento que não existe, ele retornará um erro
conjunto_d.remove(9)
print(conjunto_d)

print()
# len
print(len(conjunto_d))

print()
# in
print(5 in conjunto_d) # verifica se um objeto(5) está presente no conjunto d, retorna True se sim e False se não
print(0 in conjunto_d)

