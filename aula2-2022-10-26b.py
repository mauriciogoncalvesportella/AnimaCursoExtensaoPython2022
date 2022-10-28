nome = input('Informe seu nome:')
nota = float(input('Digite sua nota:'))

if (nota == 10):
  print(f'{nome}, você é bichão, mesmo...')

elif (nota >= 6 and nota < 10):
  print(f'{nome}, bom trabalho')

# Elif é como se fosse uma média entre um número e outro.

else:
  print(f'{nome}, você vai para a recuperação:')
