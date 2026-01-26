
sentence="The quick brown fox jumps..."
words = sentence.split()
word_length=[]

for word in words:
    if word!="the":
        word_length.append(len(word))
        print(word)
        print(word_length)

 #2 List Comprehension in one line

    wordsLenght = [len(word)for word in words if word !="the" ]
    print("This is list Comprehension")
    print(wordsLenght)

 #3 New list w positive nums