# comando input(): quero permitir que o usuário digite algo..

nome = input('Digite seu nome:')
sobrenome = input('Digite seu segundo nome:')
idade = int(input('Digite sua idade:'))
rg = int(input('Digite seu rg:'))

dobro = idade * 2


#comando de saída ...exibir na tela input
# Se quisesse mostrar o dobro da idade informada ?

print('O dobro da idade informada é {}'.format(dobro))
print(f'Seu nome é {nome}')
print(f'Seu sobrenome é {sobrenome}')
print(f'Sua idade é {idade}')
print(f'Seu registro é {rg}')

#print(f'Boa noite, seu nome é {nome}, {sobrenome} , {idade} , {rg}')

#print('Boa noite, seu nome é {}, seu sobrenome é {}, sua idade é: {} e número de registro é 123638069'.format(nome, sobrenome, idade, rg))

#print(sobrenome)
#print(idade)
#print(rg)