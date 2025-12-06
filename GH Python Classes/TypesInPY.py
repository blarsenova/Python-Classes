# Integer is a whole number, can be positive and negative
# Float is decimals
# Variable is a container
y=7.0
x=9.9
myfloat = float(x)
print(myfloat)

a, b, c = 1,2,4
print(a,b,c)

remainder =10%2.4
print(remainder)

multiplying= 7*2
squared =7**2
cubed = 2**3
print(multiplying, squared, cubed)

lotsofhellos = "hello"*9
print(lotsofhellos)

####### Lists######

myList =[1,2,3]
myList.append(6)
print(len(myList))

myListNames = ['Moe', 'Zoe', 'Zee']
myListNames.insert(1, 'Bee')
print(myListNames)

myListNames.extend(['New Name Extended here'])
print(myListNames)
myListNames.index('Moe')
print(myListNames.index('Zoe'))
myListNames.sort()
print(myListNames)

