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

# Set Difference (Unique to One Set) In math, this is $A - B$
required_tools = {"IntelliJ", "Docker", "Git", "Postman"}
installed_tools = {"Git", "IntelliJ"}

# Find what still needs to be installed (Difference)
missing_tools = required_tools - installed_tools

print(f"Please install: {missing_tools}")
# Output: {'Docker', 'Postman'}


#Symmetric Difference (The "Unique to Each" Logic)
version_1_configs = {"port:8080", "timeout:30", "retry:true"}
version_2_configs = {"port:8080", "timeout:60", "retry:true", "cache:false"}

# Symmetric Difference (Elements in one or the other, but not both)
changes = version_1_configs ^ version_2_configs

print(f"Differences detected: {changes}")
# Output: {'timeout:30', 'timeout:60', 'cache:false'}

# Define the sets
user_permissions = {"READ", "WRITE", "EXECUTE", "DELETE_USER"}
required_for_action = {"WRITE", "DELETE_USER"}

# Check if required_for_action is a SUBSET of user_permissions
# In Python, the <= operator checks for subsets
has_access = required_for_action <= user_permissions

if has_access:
    print("Access Granted: All required permissions are present.")
else:
    print("Access Denied: Missing permissions.")


    # Define user interest profiles as sets
user_a_interests = {"coding", "hiking", "sci-fi", "gaming", "coffee"}
user_b_interests = {"hiking", "photography", "coffee", "traveling", "baking"}

# 1. Intersection: Find shared interests (Mutuals)
shared = user_a_interests.intersection(user_b_interests)

# 2. Difference: Find what User A likes that User B doesn't (Personalized Recs)
unique_to_a = user_a_interests.difference(user_b_interests)

# 3. Union: Get a master list of all unique hobbies across both users
all_hobbies = user_a_interests.union(user_b_interests)

# 4. Symmetric Difference: Hobbies that only one person has, but not both
divergent_hobbies = user_a_interests.symmetric_difference(user_b_interests)

# --- Display Results ---
print(f"Shared Interests: {shared}")
print(f"Suggest to User B (from A's list): {unique_to_a}")
print(f"Total Unique Hobbies: {len(all_hobbies)}")

# 5. Membership & Modification (Medium Level)
# Checking if a specific set of tags exists in a user's profile
must_have_tags = {"hiking", "coffee"}

if must_have_tags.issubset(user_a_interests):
    print("\nUser A is a 'Nature & Cafe' enthusiast.")

# Removing duplicates from a messy list using set casting
messy_tags = ["coding", "gaming", "coding", "sci-fi", "gaming", "gaming"]
cleaned_tags = list(set(messy_tags))
print(f"Cleaned Tags: {cleaned_tags}")

