# Exercicío 6
notas = [float (input (f'Escolha a nota {i+1}:')) for i in range (3)]
media = sum(notas) / len(notas)
print (f'A média aritmética é: {media}:')