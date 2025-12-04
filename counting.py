'''
Goal: Use dictionaries to count occurrences.
'''

# Create a 'grades' list containing: ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]
grade_list: list[str] = ["A", "B", "A", "C", "B", "A", "D", "B", "C", "A"]

# Create an empty 'count' dictionary
count: dict[str, int] = {}

# Iterate over the 'grade_list' and count how many times each grade appears in the dictionary
for grade in grade_list:
    # 1. Check if the grade is already a key in the dictionary
    if grade in count:
        # If present, increment the count by 1
        count[grade] += 1
    else:
        # If not present, add the key and initialize the count to 1
        count[grade] = 1

# Print the final dictionary
print(count)