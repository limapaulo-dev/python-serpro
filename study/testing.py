import functools
import builtins

a = ("h", "b", "a", "c", "f", "d", "e", "g")
lis = [1, 3, 4, 10, 4]

x = sorted(a)
y = list(reversed(a))

filterFunc = lambda x : x == "a"
intSum = lambda a, b : a + b

filtered = list(filter(filterFunc, a))

listSum = functools.reduce(intSum, lis)

print(a)
print(x)
print(y)
print(filtered)
print(listSum)
print(sum(lis))

print(dir(builtins))
print(dir(functools))