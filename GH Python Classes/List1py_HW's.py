
#B

allWords= ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
listX=[]
plainList=[]

for words in allWords:
    if words.startswith('x'):
        listX.append(words)
        #print(sorted(listX))
    else:plainList.append(words)


print(sorted(listX) + sorted(plainList))

