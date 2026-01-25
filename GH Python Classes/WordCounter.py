
print("Tell me something and I will count words inside")
wordsCount ={}
usersInput=input('Please enter your sentence here')
words = usersInput.lower().split()

for word in words:
    if word in wordsCount:
        wordsCount[word] += 1
    else:
        wordsCount[word] = 1


print(len(wordsCount) )
print("\nWord occurrences:")
for word, count in wordsCount.items():
    print("- %s: %d" % (word, count))



