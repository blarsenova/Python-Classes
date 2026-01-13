#A

def donuts(count):
        if count >= 10:
            display_count = 'many'
        else:
            display_count = str(count)
        return 'Number of donuts: ' + display_count

print(donuts(3))
print(donuts(19))