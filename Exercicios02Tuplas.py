num = (int(input('Digite um número: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: '))
       )
print(f'O valor 9 apareceu {num.count(9)} vezes')
print(f'O valor 3 apareceu na {num.index(3)+1}ª posicao')
print('Os valores pares digitados foram: ', end="")
for n in num:
    if n % 2 == 0:
        print(n, end="")
