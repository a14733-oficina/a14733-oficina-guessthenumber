import random
nome =str(input("Insira o seu nome: "))
print("Tem 6 tentativas")
aleatorio = random.randint(1,21)#escolhe um  numero de 1 a 20 
tentativas = 6
while tentativas > 0:
    num = int(input("Insira o seu numero: "))
    if num == aleatorio:
        print("Acertas-te")
        exit()#caso o user acerte sai do programa 
    elif num > aleatorio:
        print("Numero incorreto, inferior")
        tentativas -=1#menos 1 tentaviva das 6 q tinha
        print(f"Tens {tentativas} tentativas.")
    elif num < aleatorio:
        print("Numero incorreto, superior")
        tentativas -=1
        print(f"Tens {tentativas} tentativas.")
print(f"Acabaram as tentativas o numero era{aleatorio}.")
