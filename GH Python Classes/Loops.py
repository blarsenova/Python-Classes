
primes = [2,4,6,7]

for x in primes:
    print(x)
    print('------')
    x=10
    print(x)

    #########

for x in range (3, 8):
    print(x)

    ######

    count = 0
    while (count)<5:
       # print(count)
        count+=1
       # print('while loop exited')

        #####

        count=0
        while True:
            print(count)
            count+=1
            if count>=5:
                break


        ####

    print('***** below')
    for x in range(10):
        if x%2 == 0:
            continue
    print(x)
else:print('this is else')