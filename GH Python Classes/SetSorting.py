# A list of orders that has some duplicates
orders = ["croissant", "baguette", "croissant", "macaron", "baguette"]

# Convert the list to a set to automatically remove duplicates
unique_orders = set(orders)

print(unique_orders)
# Output: {'baguette', 'macaron', 'croissant'} (The order might vary!)


# Two sets of programming languages
baktygul_skills = {"Java", "Python", "SQL"}
job_requirements = {"Python", "C++", "SQL", "AWS"}

# Find skills that match the job (Intersection)
matching_skills = baktygul_skills & job_requirements

print(f"Matches found: {matching_skills}")
# Output: {'Python', 'SQL'}