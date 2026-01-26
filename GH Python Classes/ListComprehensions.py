
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

numbers = [34.6, 6, -7, 0, 123, 432.0, 232]

# Changed 'numbers' to 'nums' inside the int() function
newList = [int(nums) for nums in numbers if nums > 0]

print(newList)
# Output: [34, 6, 123, 432, 232]