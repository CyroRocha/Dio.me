texto = "Python de Mithra"
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = " ")
else: 
    print()
    print('Executa no final do laço')

list(range(4))