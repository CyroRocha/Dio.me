def somar (a,b):
    return a + b

def subtrair (a,b):
    return a - b

def test(a,b):
    return a *2 + b *3

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f" O resultado da operação é de = {resultado}")

exibir_resultado(12,13,subtrair)
exibir_resultado(12,13,somar)

op = somar

print(op(1,23))