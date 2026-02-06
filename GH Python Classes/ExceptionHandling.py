def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
           do_stuff_with_number('n')

catch_this()


#2 Try to open a file that does not exist (e.g., file.txt).


try:
    f=open('/Users/baktygullarsenova/HelloWorld/Test python file 1', 'r')
    print("This is a try block")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("_______________________________")
    print("Sorry, that file doesn't exist")

finally:
    print("final block is : Execution completed")

