
#D - verbing
def verbing(s):
    # Check length first
    if len(s) < 3:
        return s

    # If length is 3 or more, check the ending
    if len(s) >= 3 and s.endswith('ing'):
        s += 'ly'
    else:
        s += 'ing'

    return s

def main():
    print('verbing')

#E - not bad




