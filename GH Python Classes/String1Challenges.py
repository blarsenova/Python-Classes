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
