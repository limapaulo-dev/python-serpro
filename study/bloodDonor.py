print("------------- posso doar sangue? ------------")

idade = int(input("Qual a sua idade? Ex: 35 "))
peso = int(input("Qual o seu peso? Ex. 70 "))
sono = int(input("Quanto você dormiu nas ultimas 24hs? Ex: 8h "))

if idade > 15 and idade < 70 and peso > 50 and sono > 6:
    print("-----------você pode doar sangue -----------")
else:
    print("-----------você não pode doar sangue -----------")