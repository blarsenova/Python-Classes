def find_vowels(text):
    # Define a string containing all vowels (both cases)
    vowels = "aeiouAEIOU"

    # Use list comprehension to find all vowels in the input text
    found_vowels = [char for char in text if char in vowels]

    return found_vowels

# Example usage:
input_string = "This is your captain speaking"
result = find_vowels(input_string)

print(f"Vowels found: {result}")
print(f"Total count: {len(result)}")