adobe = ['Adobe','e-mail','dica','senha','nome']
apollo = ['Apollo','e-mail','nome','telefone']
canva = ['Canva','e-mail','nome','senha']
pdl = ['PDL','e-mail','nome','telefone']
hurb = ['Hurb','e-mail','senha','telefone']
lista_primaria = [adobe, apollo, canva, pdl, hurb]
lista_senha = []
lista_email = []
for i in range(len(lista_primaria)):
    if 'senha' in lista_primaria[i]:
        lista_senha.append(lista_primaria[i][0])
    if 'e-mail' in lista_primaria[i]:
        lista_email.append(lista_primaria[i][0])
print(str(lista_senha))
print(str(lista_email))