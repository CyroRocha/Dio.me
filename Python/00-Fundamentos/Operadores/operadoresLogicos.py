print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or True)
print(False or False)

saldo = 1000
saque = 200
limite = 100
conta_especial = True

conta_normal_saldo_suficiente = saldo >= saque and saque <=limite
conta_especial_saldo_suficiente = conta_especial and saldo >= saque

exp = saldo >= saque and saque <=limite or conta_especial and saldo >= saque
print(exp)

exp2 = (saldo >= saque and saque <=limite) or (conta_especial and saldo >= saque)
print(exp2)

exp3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print(exp3)


contatos_emergencia = []
not 1000 > 1500
not contatos_emergencia
not "Saque 1500;"
not " "
