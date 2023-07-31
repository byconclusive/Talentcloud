# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)


# Imprimir todos números exceto 13(laço "for... in range")
numero = 21
for i in range(21):
  numero = numero - 1
  if (numero == 13):
    continue
  print (numero)

  # Imprimir todos os números exceto 13 (laço "while")
  contador = 13
  while (contador <= 20):
  	if (contador == 13):
  		contador = contador + 1
  		continue
  	else:
  		print(contador)
  		contador = contador + 1

 # Imprimir todos os números exceto 13 em ordem descendentes
 for i in range (20, 0, -1):
 	if (i == 13):
 		continue
 	else:
 		print(i)