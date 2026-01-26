from operator import itemgetter

#B

allWords= ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
listX=[]
plainList=[]

for words in allWords:
    if words.startswith('x'):
        listX.append(words)
        #print(sorted(listX))
    else:plainList.append(words)


print(sorted(listX) + sorted(plainList))   #print(sorted(grade, key=itemgetter(0,-1)))

#C - tuples, sorted by increasing last number
tuple1=[(1,7), (5,3), (1,4,4), (2,2), (2,8), (1,1)]
print(sorted(tuple1, key=itemgetter(-1)))



