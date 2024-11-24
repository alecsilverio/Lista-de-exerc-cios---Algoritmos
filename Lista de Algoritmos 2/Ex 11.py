#exercicio 11
frase = input ('Digite uma frase:')
palavras = frase.lower().split()
palavras_unicas = set (palavras)
print (f'A frase contém {len(palavras_unicas)} palvras únicas.')
