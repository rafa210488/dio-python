# .append() - adiciona um novo objeto, elemento ao final da lista
lista = []

print(lista)
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)

print()
# .clear() - limpa a lista
lista.clear()
print(lista)

print()
# .copy() - esse método faz uma cópia da lista, mas em uma instância diferente,
# ou seja, os dados são copiados, porém são estruturas diferentes.

lista = [1, 'Python', [40, 30, 20]]
lista_2 = lista.copy()
print(lista_2)

print()
# .count() - é utilizado para contar quantas vezes um objeto aparece dentro da lista

cores = ['vermelho', 'azul', 'verde', 'azul']

print(cores.count('vermelho'))
print(cores.count('verde'))
print(cores.count('azul'))

print()
# .extend() - ele 'junta' uma lista a outra já existente
linguagens = ['Python', 'JavaScript', 'c']

print(linguagens)
linguagens.extend(['Java', 'Csharp'])
print(linguagens)

print()
# .index() - funciona para mostrar a primeira ocorrência de um objeto dentro de uma lista
print(linguagens.index('Java'))
print(linguagens.index('c'))

print()
# .pop() - esse método retira o último elemento da lista. 
# Podemos também passar como argumento desse método, o índice do elemento que queremos remover.
linguagens.pop() # Csharp
linguagens.pop() # Java
linguagens.pop(1) # JavaScript

print(linguagens)

print()
# .remove() - Diferente do .pop(), o método remove, remove o elemento que for passado como argumento, 
# mas aqui precisamos passar o próprio elemento e não apenas o índice.

linguagens.remove('c')
print(linguagens)

print()
# .reverse() - coloca a lista ao contrário.
cores = ['azul', 'vermelho', 'verde', 'amarelo']
cores.reverse()
print(cores)

print()
# .sort() - ordena a lista, em ordem alfabética, numérica e etc.
cores.sort()
print(cores)
cores.sort(reverse=True)
print(cores)

cores.sort(key=lambda x: len(x)) # aqui ele ordena pelo tamanho de cada elemento, 
#sendo lambda uma função anônima, que vai varrer a lista pegando o tamanho de cada string e ordenando de acordo com o tamanho.
print(cores)

cores.sort(key=lambda x: len(x), reverse=True)
print(cores)

print()
# len() - ele mostra o tamanho dos elementos, de uma string ou lista.
print(len(cores))

print()
# sort() - é uma função que trabalha basicamente da mesma forma que o sort

sorted(cores, key=lambda x: len(x))
print(cores)
print(sorted(cores, key=lambda x: len(x)))
