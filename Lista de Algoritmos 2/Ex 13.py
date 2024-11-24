#exercicio 13
def calcular_media (notas):
    return sum(notas) / len(notas)

notas = []
quantidade = int (input('Digite a quantidade de notas:'))

for i in range(quantidade):
    nota = float (input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

media = calcular_media(notas)

notas_maiores_que_a_media = [nota for nota in notas if nota > media]
print (f'A média das notas é: {media:.2f}')
print (f'As notas maiores que a média são: {notas_maiores_que_a_media}')
