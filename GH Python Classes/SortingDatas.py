from operator import itemgetter

numbers = [34.6, 6, -7, 0, 123, 432.0, 232.99]
print(sorted(numbers))

#.sort doesn't work w Dictionaries or

strs = ['aa', 'DDD', 'c', 'ca', 'AaAAA', 'FFfF']
print(sorted(strs))
print(sorted(strs, reverse=True))
print(sorted(strs, key=len, reverse=True))

#Print last letter of each string

strss=['Abba', 'Holiday', 'song']

def Myfn(s):
    return s[-1]

print(sorted(strss, key=Myfn))

#Tuples sort

grade= [('Freddy', "Aida", 3), ('Anil', 'Aneela', 1)]
print(sorted(grade, key=itemgetter(0,-1)))
