numbers=[5,2,1,7,1,4]
numbers.append(20)#adiciona no final
print(numbers)
numbers.insert(0,10)#escolhe local e adiciona
print(numbers)
numbers.remove(5)#remove
print(numbers)
#numbers.clear()#remove tudo
numbers.pop()#remove o ultimo  item  da lista 
print(numbers.index(1))#aonde tá o valor 
print(50 in numbers)#verifica se tem o valor na lista boolean
print(numbers.count(1))#quantidade que aparece
numbers.sort()#arruma a lista crescente
numbers.reverse()#decrescente
num=numbers.copy()#copia a lista
