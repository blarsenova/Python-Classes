

phonebook ={"John": 123, "Doee": 456, "Jill":789}

for name, number in phonebook.items():
    print("phone number of %s is %d" %(name, number))

    del phonebook["John"]
    #print(phonebook + 'after deletion')
    phonebook.pop("Jill")
    print(phonebook)