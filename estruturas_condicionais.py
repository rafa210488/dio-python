MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade. Pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
    print('Não tem idade para tirar CNH, mas pode fazer as aulas teóricas')
else:
    print('Ainda não pode tirar CNH')

    