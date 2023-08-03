# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
# O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
# No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
# o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, 
# um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, 
# E o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

#------ Resposta --------
def calculadora():

	while True :
		numero1 = float(input("Digite o primeiro número: "))
		numero2 = float(input("Digite o segundo número: "))	
		operacao = int(input("Operações: 1 - soma; 2 Subtração; 3 - Multiplicar; 4 - Divisão; 0 - Sair! Digite a operação: "))
	
		if operacao == 0:
			break
		elif operacao == 1:
			return print(numero1 + numero2)
			
		elif operacao == 2:
			return print(numero1 - numero2)
			
		elif operacao == 3:
			return print (numero1 * numero2)
	 
		elif operacao == 4:
			if numero2 == 0:
				print("Número não é dividivo por zero! Tente de novo!")
			else: 
				return print (numero1 / numero2)
		else:
			print("Opção errada, tente de novo!")
		
calculadora()