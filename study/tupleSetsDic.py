# python não tem arrays, mas tem listas, tuplas, sets, dicionários
# além de listas podemos usar tuple, sets and dicionáries  


tuple1 = ("segunda", "terça","quarta","quinta","sexta")
# tuples bão podem ser modificadas depois de inicializadas 
# usam menos memória

set1 = {"segunda", "terça","quarta","quinta","sexta"}
# sets não aceitam elementos repetidos não tem index
# sets não tem ordem e não podemos modificar os elementos
# sets podem ter elementos removidos e adicionados 
set1.add('domingo')
set1.remove('segunda')

dic1 = {"nome" : "paulo", "peso" : 70, "idade" : 35}
# dicionários recebem valores no modelo chave:valor 
# dicionários não aceitam chaves repetidas 
# não tem index, para chamar elementos usamos as chaves
dic1["nome"] 

dic1["sobrenome"] = "alves de lima"
dic1["peso"] = 75
dic1.update({"nome": "paulo ricardo"})
dic1.pop("sobrenome")

print(dic1)

print(tuple1[0])

print(set1)

print(dic1["nome"])


