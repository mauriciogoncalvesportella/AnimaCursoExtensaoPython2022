print('Início da aula 3 (09/11/2023)')

contador = 1
#Exibir de 1 até 10 repetidamente
while(contador <=10):
  print(contador)
  contador = contador+1 #contador += 1

#Laço for (python for = for each)

fruta = 'morango'
print(fruta)

fruta1 = 'morango'
fruta2 = 'laranja'
fruta3 = 'pêra'

#Lista []
frutas = ['morango', 'laranja', 'pêra']
print(frutas) # Mostra todas dessa forma.

#Quero exibir apenas a pêra. fruta (pêra)
#Onde está os nomes das frutas ele conta a partir de 0 e não de 1, por isso o número 2 da lista [2]
print(frutas[2])

#Quantas frutas tem na minha lista ?
print(len(frutas)) # length = tamanho

#Quero incluir uma fruta nova
frutas.append('manga')

print(len(frutas))
print(frutas)

print('Exemplo das frutas com while')


print(frutas[0])

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print('Exemplo das frutas com o FOR')
for fruta in frutas:
  print(fruta)
