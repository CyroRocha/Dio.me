nome = "Gabriel"
idade = 25
profissao = "Programador"
linguagem = "Python"
saldo = 45.434

dados = {"nome":"Gabriel","idade": 25,"profissao": "Programador",
"linguagem":"Python"}
PI = 3.14159

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f'Nome: {nome} Idade: {idade}')
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}' )