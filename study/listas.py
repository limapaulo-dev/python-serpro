# python não tem arrays, mas tem listas, tuplas, sets, dicionários


# listas podem ter elementos diversos
lista1 = ["maça", 57, "lucas", 115.5, "eu tenho 35 anos", True, [25, 45, 22]]
listaBool = [True, False, True, False, True, True, False]
listaAge = [35, 33, 35, 44, 78, 2 ,4 ,5 ,55]
listaPrice = [21.55, 57.54, 87.50, 7.54, 5, 55]

print("lista1: ")
print(lista1)
print()
print("lista1[0] acessa o index 0")
print(lista1[0])
print()
print("lista1[1:3] imprime index 1 até 2")
print(lista1[1:3])
print()

lista1.append("compass")
lista1.insert(1, "orange")
print(lista1)
print()

lista1.remove("compass")
lista1.pop(0)
print(lista1)
print("maça" not in lista1)

print(lista1.count("maça"))
print(len(lista1))
print(listaBool.sort())
print(listaBool)
print(listaAge.sort())
print(listaAge)
print(any(listaAge))
print(any(listaBool))
print(all(listaBool))
print(lista1.clear())

def inflation(x):
  return x * 10
inflation = lambda x : x * 10

inlfationList = list(map(inflation, listaPrice))

print("Lista de preços")
print(listaPrice)
print("map listaPrice + inflation func")
print(inlfationList)