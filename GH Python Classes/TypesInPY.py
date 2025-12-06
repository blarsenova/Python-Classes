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
myListNames.reverse()
print(myListNames)

my_Element= myListNames.pop(0)
print(my_Element)
print(len(myListNames))

####input thru Terminal####
myInput = input()
print(myInput)

num=int(input())
print(num)

#####output formatting####
a=5.009
b=0.63
c="good morning"
print("a is %d, b is %0.9f, c is %s" % (a,b,c))

