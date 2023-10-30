#aula 28 ----------------------------------------
from sys import getsizeof

valores = [x * 10 for x in range(10)]
print (getsizeof(valores))

print ('======')

valores = (x * 10 for x in range (10))
print(getsizeof(valores))