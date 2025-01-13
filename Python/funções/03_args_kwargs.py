def exibir_poema(data_extenso, *lista, **dicionario):
    texto ="\n".join(lista)
    meta_dados ="\n".join([f"{chave.title()}: {valor}" for chave,valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "segunda, 13 de janeiro de 2024",
    "Zen of Python",
    "Bonito é melhor que feio.",
    "Explícito é melhor que implícito.",
    "Simples é melhor que complexo.",
    "Complexo é melhor que complicado.",
    "Linear é melhor do que aninhado.",
    "Esparso é melhor que denso.",
    "Legibilidade conta.",
    "Casos especiais não são especiais o bastante para quebrar as regras.",
    "Ainda que praticidade vença a pureza.",
    "Erros nunca devem passar silenciosamente.",
    "A menos que sejam explicitamente silenciados.",
    "Diante da ambiguidade, recuse a tentação de adivinhar.",
    "Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo.",
    "Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.",
    "Agora é melhor que nunca.",
    "Apesar de que nunca normalmente é melhor do que *exatamente* agora",
    "Se a implementação é difícil de explicar, é uma má ideia",
    "Se a implementação é fácil de explicar, pode ser uma boa ideia",
    "Namespaces são uma grande ideia — vamos ter mais dessas!", 
    autor = "Tim Peters", 
    ano = 1999)