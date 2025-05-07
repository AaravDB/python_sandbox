# A List is a collection which is ordered and changeable. Allows duplicate members.
a=[1,2,3,4,5,6,7,8]
print(a)

fruits=['Apples','Oranges','Grapes','Pears']
print(fruits[1])
print(len(fruits))
fruits.append('Mangos')
print(fruits)
fruits.insert(2,'bananas')
print(fruits)
fruits.pop(3)
print(fruits)
#len,insert,pop,sort,reverse
fruits.reverse()
print(fruits)
fruits.sort(reverse=True)
print(fruits)