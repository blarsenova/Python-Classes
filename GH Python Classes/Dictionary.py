

phonebook ={"John": 123, "Doee": 456, "Jill":789, "Me":1, "You":2}

for name, number in phonebook.items():
    print("phone number of %s is %d" %(name, number))

    del phonebook["John"]
    #print(phonebook + 'after deletion')
    phonebook.pop("Jill")
    #print(phonebook)


    #2
    dict1 ={"one":1, "two":2, "three":3, "four":4}
    for key in dict1:
        print(key)
        print(dict1.keys())
        print("%s are the values" % dict1.values())
        break

    #3 sorted

    for key in sorted(dict1.keys()):
        print(key, dict1[key])

    #4 Dict Formatting

    h={}
    h['word']= 'garfield'
    h['count']=42
    s= 'I want $(count)d copies of %(word)s' %h
    print(h)
