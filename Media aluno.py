

n1 = int (input ('Digite a primeira nota:'))
n2 = int (input ('Digite a segunda nota:'))
soma = n1+n2
print('\033[0mMedia final {}'.format(soma'))
if soma >=7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')