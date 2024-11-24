# Exercicío 5
numero = int (input ('Escolha um numero para ver a tabuada:'))
print(f'Tabuada do {numero}:')
for i in range (0, 11): # Porque 11 e não 10
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    
