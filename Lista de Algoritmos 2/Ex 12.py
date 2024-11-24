#exercicio 12
def eh_primo(num):
    if num < 2:
        return False
    for i in  range (2, int (num**0.5) + 1):
        if num % i == 0:
            return False
    return True
inicio = int (input ('Digite o início do intervalo: '))
fim = int (input ('Digite o fim do intervalo: '))

primos = [num for num in range ( inicio, fim + 1) if eh_primo(num)]
print (f'Os números primos no intervalo de {inicio} a {fim} são: {primos}' )
