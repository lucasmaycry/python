import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
ordem = [a1, a2,a3,a4]
random.shuffle(ordem)
print('A ordem de apresentação será:')
print(ordem)