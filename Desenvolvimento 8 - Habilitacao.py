print("Bem vindo. Sua habilitação está quase pronta.");
rodas = int(input("Qual a quantidade de rodas? "));
peso = float(input("Qual a quantidade de peso? "));
pessoas = int(input("Qual a quantidade de pessoas? "));


if rodas == 2 or rodas == 3 and pessoas <= 2 and peso < 3500:
    print("Sua habilitação é A");
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("Sua habilitação é B");
elif rodas >= 4 and peso > 3500 and peso <= 6000:
    print("Sua habilitação é C");
elif rodas >= 4 and pessoas > 8:
    print("Sua habilitação é D");
elif rodas >= 4 and peso > 6000:
    print("Sua habilitação é E");