
def isValid():
    # 1. Get the input from the user
    s = input("Enter the parentheses string (e.g., ()[]{}): ")

    # 2. A valid string must have an even length
    if len(s) % 2 != 0:
        print("Result: False")
        return

    # 3. Repeatedly remove matching pairs
    # This loop runs as long as any matching pair exists in the string
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")

    # 4. Check if the string is empty
    if s == "":
        print("Result: True")
    else:
        print("Result: False")

# Call the function to run it
isValid()