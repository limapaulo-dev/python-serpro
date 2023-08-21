names = ["maria", "tommy", "jack", "lucy"]
numbs = [3, 5, 7, 8 ,1 ,54, 4]

inflation = lambda x : x * 10
inflationNumbs = []

for x in numbs:
    inflationNumbs.append(inflation(x))

print(inflationNumbs)