# Desenvolvimento 10 - Calculadora
# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a  operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite a operação: "))




def calculadora(numero1, numero2, operacao):
	if operacao == 1:
		print(numero1 + numero2)

	elif operacao == 2:
		print(numero1 - numero2) 

	elif operacao == 3:
		print (numero1 * numero2)

	elif operacao == 4:
		print (numero1 / numero2) 

	else:
		print("0,opção errada, tente de novo!")

calculadora(numero1, numero2, operacao)