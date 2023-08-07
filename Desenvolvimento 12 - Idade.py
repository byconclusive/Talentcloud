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
