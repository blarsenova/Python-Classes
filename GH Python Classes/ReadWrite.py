
# Open the file you just created
f = open('/Users/baktygullarsenova/HelloWorld/Test python file 1', 'rt', encoding='utf-8')

for line in f:
    print(line, end='')

f.close()

path = '/Users/baktygullarsenova/HelloWorld/Test python file 1.txt'

#with open('/Users/baktygullarsenova/HelloWorld/Test python file 1.txt', 'w') as f:
 #   f.write('This is custom msg string')
# Step 1: Write to the file

f2 = open(path, 'w', encoding='utf-8')
f2.write('This is custom msg string')
f2.close() # You MUST close it to save the changes before reading

# Step 2: Read from the file
f2 = open(path, 'rt', encoding='utf-8')
for line in f2:
    print(line, end='')
f2.close()

# Step 1: Write to the file
f2 = open(path, 'w', encoding='utf-8')
f2.write('This is custom msg string')
f2.close() # You MUST close it to save the changes before reading

# Step 2: Read from the file
f2 = open(path, 'rt', encoding='utf-8')
for line in f2:
    print(line, end='')
f2.close()


