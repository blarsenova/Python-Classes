#A

def donuts(count):
        if count >= 10:
            display_count = 'many'
        else:
            display_count = str(count)
        return 'Number of donuts: ' + display_count

print(donuts(3))
print(donuts(19))


#C
def fix_start(s):

    front = s[0]

    back = s[1:]

    # Replace the front character inside the back string
    replaced = back.replace(front, '*')

    # Combine them back together
    return front + replaced

print(fix_start("babble"))
print(fix_start("vveryyy"))

#D

def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]

    return a_swapped + ' ' + b_swapped

print(mix_up('dog', 'dinner'))

# In, Is, Not
print('==============')
a=2
a==2

x=[1,2,3]
y=[1,2,3]
z=x
print(x==y)
print(x is y) # IS looks for a memory address, under the hood
print(z is x)

print('-----------')
print(not False) #true
print((not False)== (False))

