texto = input('Digite um texto: ')
VOGAIS = 'AEIOU'

# Exemplo utilizando um objeto iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
print()       

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=' ')
    