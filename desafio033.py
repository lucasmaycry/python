a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
#testar o menor
menor= a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor=c
#testando o maior
maior= a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))