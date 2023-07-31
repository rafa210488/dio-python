# Criando um dicionário
pessoa = {'nome': 'Rafael', 'idade': 35}

pessoa_2 = dict(nome= 'Rafael', idade= 35)

pessoa_2['telefone'] = '3333-1234'
print(pessoa)
print(pessoa_2)

print()
# Acesso aos dados
print(pessoa_2['nome'])
print(pessoa_2['telefone'])

print()
# Dicionários aninhados
contatos = {
    'rafael@gmail.com': {"nome": "Rafael", "idade": 35},
    'karina@gmail.com': {"nome": "Karina", "idade": 32}
}

print(contatos['karina@gmail.com']['idade'])

print()
# Iterando sobre um dicionário
for chave in contatos:
    print(f'{chave}: {contatos[chave]}')

print()

for chave, valor in contatos.items():
    print(f'{chave}: {valor}')

print()
# MÉTODOS DA CLASSE DICT
# clear()
print(pessoa)
pessoa.clear()
print(pessoa)

print()
# copy()
pessoa = pessoa_2.copy()
pessoa['nome'] = 'Rafa'
print(pessoa)
print(pessoa_2)

print()
# fromkeys()
pessoa_3 = dict.fromkeys(['nome', 'idade']) # aqui ele cria as chaves com valor None
pessoa_4 = dict.fromkeys(['nome', 'idade'], 'Rafa') # aqui as mesmas chaves são criadas, mas com o valor padrão passado como argumento 'Rafa'
print(pessoa_3)
print(pessoa_4)

print()
# get()
print(pessoa)
print(pessoa.get('endereço')) # aqui o retorno será None, pois não existe a chave endereço
print(pessoa.get('endereço', {})) # aqui o retorno será {}, pois ao procurar a chave endereço e não encontrar, pedimos ao sistema que retorne um dicionário vazio({})
print(pessoa.get('nome', {})) # aqui passamos uma chave existente, então o sistema acessa o valor da chave

print()
# items()
print(contatos)
print(contatos.items()) # retorna uma lista de tuplas com os itens do nosso dicionário

print()
# keys()
print(pessoa)
print(pessoa.keys()) # retorna uma lista com as chaves do nosso dicionário

print()
# pop()
print(pessoa)
resultado = pessoa.pop('telefone')
print(resultado)
print(pessoa)
resultado = pessoa.pop('telefone', 'não encontrei a chave')
print(resultado)

print()
# popitem()
print(contatos)
print(contatos.popitem()) # remove o primeiro item do dicionário, e retornará erro caso não ache itens 

print()
# setdefault()
contato = {'nome': 'Rafael', 'telefone': '3333-2121'}

contato.setdefault('nome', 'Rafa') # aqui a chave nome já existia no dicionário, então o comando foi desconsiderado, mantendo a chave e valor já existentes
print(contato)
contato.setdefault('idade', 35) # aqui a chave idade não existia, então foi adicionada junto com o valor passado
print(contato)

print()
# update()
contatos_2 = {
    'rafael@gmail.com': {"nome": "Rafael", "idade": 35}
}
print(contatos_2)
contatos_2.update({"rafael@gmail.com": {"nome": "Rafa", "telefone": "3333-2211"}}) # aqui ele atualiza a chave já existente com outro dicionário com valores diferentes
print(contatos_2)
contatos_2.update({'karina@gmail.com': {'nome': 'Karina'}})
print(contatos_2)

print()
# values()
print(contatos_2.values())


print()
# in
resultado = 'rafael@gmail.com' in contatos_2 # verifica se a chave passada existe no dicionário
print(resultado)
result = 'isadora@gmail.com' in contatos_2
print(result)
resultado_2 = 'telefone' in contatos_2['rafael@gmail.com'] # verifica se existe a chave telefone do dicionário rafael@gmail.com que é uma chave do dicionário contatos_2
print(resultado_2)
resultado_3 = 'idade' in contatos_2['karina@gmail.com']
print(resultado_3)

print()
# del
print(contatos_2)
del contatos_2['karina@gmail.com'] # deleta completamente a chave karina@gmail.com do dicionário
print(contatos_2)
del contatos_2['rafael@gmail.com']['telefone'] # aqui o caminho passado foi da chave de um dicionário interno ao principal, e esta chave será excluida
print(contatos_2)
