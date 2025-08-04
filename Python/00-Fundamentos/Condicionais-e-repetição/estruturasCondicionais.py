saldo  = 2000.0
opcao = int(input("Informe uma opção : [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    saque = float(input("informe o valor do saque"))

    if saldo >= saque:
        print("Realizando saque!")

    if saldo < saque:
        print("Saldo insuficiente!")

elif opcao == 2:
    print("Exibindo o extrato ...")
    print(f'O saldo é {saldo}')

else:
    print("Opção inválida")

Maior_idade = 18
Idade_especial = 17
idade = int(input("informe sua idade: "))

if idade >= Maior_idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade == Idade_especial :
    print('Pode fazer aulas teóricas, mas não pode fazer aulas práticas.')
else:
    print("Ainda não pode tirar a CNH.")