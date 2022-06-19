adobe = ['Adobe',2013.10,'e-mail','dica','senha','nome']
apollo = ['Apollo',2018.7,'e-mail','nome','telefone']
canva = ['Canva',2019.5,'e-mail','nome','senha']
pdl = ['PDL',2019.10,'e-mail','nome','telefone']
hurb = ['Hurb',2019.4,'e-mail','senha','telefone']
animoto = ['Animoto',2018.7,'e-mail','senha']
appen = ['Appen',2020.6,'e-mail','nome','senha','telefone']
teespring = ['Teespring',2020.4,'e-mail','nome']
vk = ['VK',2012.1,'nome']
tumblr = ['Tumblr',2014.5,'dica']
streeteasy = ['StreetEasy',2019.3,'telefone']
storybird = ['StoryBird',2017.4,'e-mail']
snail = ['Snail',2015.8,'e-mail','telefone','senha']
shein = ['Shein',2018.7,'e-mail','telefone']
shopback = ['ShopBack',2014.12,'e-mail','telefone','senha']
lista_primaria = [shopback, shein,snail,storybird,streeteasy,tumblr,vk,teespring,appen,animoto, adobe, apollo, canva, pdl, hurb]
lista_senha_desordenado = []
lista_senha_comparativo_datas = []
lista_senha_ordenado = []
lista_email_desordenado = []
lista_email_comparativo_datas = []
lista_email_ordenado = []
lista_dica_desordenado = []
lista_dica_comparativo_datas = []
lista_dica_ordenado = []
lista_telefone_desordenado = []
lista_telefone_comparativo_datas = []
lista_telefone_ordenado = []
lista_nome_desordenado = []
lista_nome_comparativo_datas = []
lista_nome_ordenado = []
print ('Usando como grau de criticidade e como critério de desempate a data mais recente de violação, segue a listagem:')
print ( '=' * 20 )
for i in range(len(lista_primaria)):
    if 'senha' in lista_primaria[i]:
        lista_senha_desordenado.append(lista_primaria[i][0:2])
    elif 'dica' in lista_primaria[i]:
        lista_dica_desordenado.append(lista_primaria[i][0:2])
    elif 'telefone' in lista_primaria[i]:
         lista_telefone_desordenado.append(lista_primaria[i][0:2])
    elif 'nome' in lista_primaria[i]:
        lista_nome_desordenado.append(lista_primaria[i][0:2])
    elif 'e-mail' in lista_primaria[i]:
        lista_email_desordenado.append(lista_primaria[i][0:2])
for i in range(len(lista_senha_desordenado)):
    if i == 0 or lista_senha_desordenado[i][1] < lista_senha_comparativo_datas [-1]:
        lista_senha_comparativo_datas.append(lista_senha_desordenado[i][1])
        lista_senha_ordenado.append(lista_senha_desordenado[i][0])
    else:
        pos = 0
        while pos < len(lista_senha_comparativo_datas):
            if lista_senha_desordenado[i][1] >= lista_senha_comparativo_datas[pos]:
                lista_senha_comparativo_datas.insert(pos, lista_senha_desordenado[i][1])
                lista_senha_ordenado.insert(pos, lista_senha_desordenado[i][0])
                break
            pos += 1
print(*lista_senha_ordenado, sep = ', ', end =', ')
for i in range(len(lista_dica_desordenado)):
    if i == 0 or lista_dica_desordenado[i][1] < lista_dica_comparativo_datas [-1]:
        lista_dica_comparativo_datas.append(lista_dica_desordenado[i][1])
        lista_dica_ordenado.append(lista_dica_desordenado[i][0])
    else:
        pos = 0
        while pos < len(lista_dica_comparativo_datas):
            if lista_dica_desordenado[i][1] >= lista_dica_comparativo_datas[pos]:
                lista_dica_comparativo_datas.insert(pos, lista_dica_desordenado[i][1])
                lista_dica_ordenado.insert(pos, lista_dica_desordenado[i][0])
                break
            pos += 1
print(*lista_dica_ordenado, sep = ', ', end =', ')
for i in range(len(lista_telefone_desordenado)):
    if i == 0 or lista_telefone_desordenado[i][1] < lista_telefone_comparativo_datas [-1]:
        lista_telefone_comparativo_datas.append(lista_telefone_desordenado[i][1])
        lista_telefone_ordenado.append(lista_telefone_desordenado[i][0])
    else:
        pos = 0
        while pos < len(lista_telefone_comparativo_datas):
            if lista_telefone_desordenado[i][1] >= lista_telefone_comparativo_datas[pos]:
                lista_telefone_comparativo_datas.insert(pos, lista_telefone_desordenado[i][1])
                lista_telefone_ordenado.insert(pos, lista_telefone_desordenado[i][0])
                break
            pos += 1
print(*lista_telefone_ordenado, sep = ', ', end =', ')
for i in range(len(lista_nome_desordenado)):
    if i == 0 or lista_nome_desordenado[i][1] < lista_nome_comparativo_datas [-1]:
        lista_nome_comparativo_datas.append(lista_nome_desordenado[i][1])
        lista_nome_ordenado.append(lista_nome_desordenado[i][0])
    else:
        pos = 0
        while pos < len(lista_nome_comparativo_datas):
            if lista_nome_desordenado[i][1] >= lista_nome_comparativo_datas[pos]:
                lista_nome_comparativo_datas.insert(pos, lista_nome_desordenado[i][1])
                lista_nome_ordenado.insert(pos, lista_nome_desordenado[i][0])
                break
            pos += 1
print(*lista_nome_ordenado, sep = ', ', end =', ')
for i in range(len(lista_email_desordenado)):
    if i == 0 or lista_email_desordenado[i][1] < lista_email_comparativo_datas [-1]:
        lista_email_comparativo_datas.append(lista_email_desordenado[i][1])
        lista_email_ordenado.append(lista_email_desordenado[i][0])
    else:
        pos = 0
        while pos < len(lista_email_comparativo_datas):
            if lista_email_desordenado[i][1] >= lista_email_comparativo_datas[pos]:
                lista_email_comparativo_datas.insert(pos, lista_email_desordenado[i][1])
                lista_email_ordenado.insert(pos, lista_email_desordenado[i][0])
                break
            pos += 1
print(*lista_email_ordenado, sep = ', ')
