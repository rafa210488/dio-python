# Criando uma função
def exibir_mensagem(): # forma simples de declarar uma função, sem argumentos
    print('Olá, Mundo!!')
    
# exibir_mensagem()

def exibir_mensagem_2(nome): # aqui declaramos a função agora passando uma variável como argumento
    print(f'Seja bem vindo, {nome}')

# exibir_mensagem_2('Rafael')

def exibir_mensagem_3(nome='Anônimo'): # aqui também passamos uma variável como argumento, mas agora deixamos essa variável com um valor padrão, caso ela não receba um valor na hora de ser chamada.
    print(f'Seja muito bem vindo, {nome}')

# exibir_mensagem_3()
# exibir_mensagem_3(nome='Rafa')

print()
# Retornando valores nas funções
def calcular_total(numeros): # aqui usamor o retorno de uma soma de uma lista de números
    return sum(numeros) # o retorno nesse caso só trará um valor, então podemos nesse caso printar o retorno, ou atribuir a uma variável para depois utilizar esse valor

# print(calcular_total([5, 3, 2]))

def retorna_antecessor_e_sucessor(numero): # nesta função retornamos dois valores, que também podem ser atribuídos a uma variável para posterior uso
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor # ou podemos printar o valor que será retornado
# print(retorna_antecessor_e_sucessor(10))

print()
# Argumentos Nomeados
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}')
salvar_carro('Fiat', 'Uno', 2014, 'ABC-1234') 
# ^ Dessa primeira forma, a desvantagem é que temos que passar os argumentos na ordem que foram colocados na função
# então caso, ao chamar a função os argumentos sejam passados de uma ordem errada, o python irá mostrar na ordem errada
salvar_carro(marca='Fiat', modelo='Mobi', ano=2019, placa='ABB-2525')
# ^ Dessa forma, se garante que cada argumento receberá seu valor correto, então a ordem não importará, pois cada argumento foi passado corretamente
salvar_carro(**{'marca': 'Fiat', 'modelo': 'Uno', 'ano': 2020, 'placa': 'ABC-6030'})
# ^ Dessa terceira forma, os dois asteriscos indica que estamos passando como se fosse um dicionário para os argumentos da função
# e por baixo dos panos o python coloca na forma como colocamos na saída da função
print()

# Args e Kwargs
def exibir_poema(data_extenso, *args, **Kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f"{chave.title()}: {valor}" for chave, valor in Kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)
    
exibir_poema('Zen of Python', 'beautiful is better than ugly.', autor='Tim Peters', ano=1999)

print()
# Parâmetros especiais
# Posição e nomes
def criar_carro(modelo, ano, placa, /, marca, motor, combustível): # os parâmetros antes da barra são somente por posição, aqueles após podem ser por posição ou nome
    print(modelo, ano, placa, marca, motor, combustível)

criar_carro('Uno', 2014, 'abc-2222', marca='Fiat', motor='1.0', combustível='Gasolina') # Forma válida de chamar a função
# criar_carro(modelo='Uno', ano=2014, placa='abc-2222', marca='Fiat', motor='1.0', combustível='Gasolina') # Forma inválida de chamar essa função, pois aqueles argumentos que são por posição, estão sendo passados por nome.

print()
# Apenas nomeados (Keywords)
def criar_carro_2(*, modelo, ano, placa, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível) # Nesta função, os parâmetros são todos através de keywords(nomes), sabemos disso colocando o asterisco antes dos parâmetros necessáriossssssssss

criar_carro_2(modelo='Palio', ano=2016, placa='ABC-8545', marca='Fiat', motor='1.6', combustível='Etanol') # Forma válida de chamar essa função, com todos os parâmetros sendo passados através do nome+
# criar_carro_2('Palio', 2015, 'ABB-9632', marca='Fiat', motor='1.4', combustível='Gasolina') # Forma inválida de fazer essa função, pois nem todos os parâmetros foram passados com seu nome na criação da função

print()
# Objetos de Primeira classe
def somar(a, b):
    return a + b

def exibir_resultado(a, b, função): # neste função, passamos como parâmetro uma outra função
    resultado = função(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')
    
exibir_resultado(5, 10, somar)

operacao = somar # Aqui atribuímos a uma variável a nossa função somar
print(operacao(5, 3))

print()
# Escopo local e global
salario = 2000

def salario_bonus(bonus):
    global salario # aqui estamos declarando que estamos usando a variável salario, que esta no escopo global(fora da função), e aqui nessa função, essa variável será alterada, o que vai impactar essa variável no escopo global
    salario += bonus
    return salario

novo_salario = salario_bonus(1000)
print(novo_salario)
print(salario)
