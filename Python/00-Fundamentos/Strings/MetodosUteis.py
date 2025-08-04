Nome = "miTHra"

print(Nome.upper())
print(Nome.lower())
print(Nome.title())

texto = " Olá Mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")


menu = "Python"

print("####Python####")
print(menu.center(14))
print(menu.center(14,'#'))

for letra in menu:
    print(letra, end="-")
print(" ")

print("-".join(menu))
