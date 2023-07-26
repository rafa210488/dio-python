opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))
    
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')
else:
    print('Obrigado por usar nosso sistema bancário, até logo!!')

print()

# Usando break - break para a execução
while True:
    numero = int(input('Informe um número: '))
    
    if numero == 10:
        print(f'{numero}, saindo....')
        break
    print(numero)
    
# Usando o continue - o continue pula a execução
for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero)