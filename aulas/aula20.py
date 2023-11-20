#aula 20 ----------------------------------------

list1 = [10, 20, 30, 40, 50]
list2 = [10, 30, 50, 70, 90]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2)  #Union
print(num1 & num2)  #And
print(num1 - num2)  #Diferença
print(num1 ^ num2)  #Diferença simétrica