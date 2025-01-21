def are_parentheses_balanced(input_string):
    # Stack to keep track of opening parentheses
    stack = []
    
    # Mapping of closing to opening parentheses
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in input_string:
        if char in matching_parentheses.values():  # If it's an opening parenthesis
            stack.append(char)
        elif char in matching_parentheses.keys():  # If it's a closing parenthesis
            if not stack or stack.pop() != matching_parentheses[char]:
                return False
    
    # If the stack is empty, all parentheses are balanced
    return len(stack) == 0


# Test cases
example_1 = "I { love [ the {rains}()] }"
example_2 = "I { love [ the {rains ] ()"

# Output results
print(f"Example 1: {are_parentheses_balanced(example_1)}")  # Output: True
print(f"Example 2: {are_parentheses_balanced(example_2)}")  # Output: False