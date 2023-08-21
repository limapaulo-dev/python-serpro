import builtins

builtinsList = dir(builtins)
indexTrash = builtinsList.index('__spec__')

print(builtinsList[indexTrash+1:])