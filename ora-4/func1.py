from random import randint



lista = [randint(1, 10) for _ in range(10)]

eredmeny = [(i,x) for i, x in enumerate(lista)]

print(list(enumerate(lista)))
for index, elem in enumerate(lista):
	print(index, elem)
