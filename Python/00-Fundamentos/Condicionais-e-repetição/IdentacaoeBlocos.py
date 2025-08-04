def sacar(valor:float) -> None:
    saldo = 500
    
    if saldo >= valor:
        print("valor sacado")
        saldo -= valor
        print('Retire seu dinheiro na boca do caixa')
    else :
        print('Saldo indisponivel')      
    print('Obrigado por ser nosso Cliente, Tenha um bom dia!')

def depositar(Valor:float):
    saldo = 500
    saldo += Valor
    print("valor depositado")
    print(f'O Novo saldo é {saldo}')


sacar(100)
depositar(100)