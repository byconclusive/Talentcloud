# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, 
# no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


# ---- Resposta ---

def idade ():
  while True :
    print("Saudações! Descubra sua idade a seguir!")
    nomecompleto = str(input("Digite seu nome Completo: "))
    anonascimento = int(input("Digite o ano do seu nascimento: "))

    try:
      if anonascimento < 1922 or anonascimento > 2021:
        print("Dados não podem ser calculados! Tente de novo!")
      else:
        print(nomecompleto, "sua idade é" ,2021 - anonascimento)
        print("Obrigado por usar nosso sistema!")
        break
    except:
        nomecompleto != str or anonascimento != int
        return ("Dados incorretos. Tende de novo!")
idade()
