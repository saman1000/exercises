# Create a function that determines the minimum number of bracket removals needed for a valid string.
def min_removals_to_balance(brackets):
    # TODO: Initialize an empty list to act as the stack
    stack = []

    # TODO: Iterate through each bracket in the input string
    index = 0
    required_removals = 0
    while index < len(brackets):
        # TODO: Add conditions to handle the opening and closing brackets appropriately using stack operations
        if brackets[index] == '(':
            stack.append(brackets[index])
        elif brackets[index] == ')':
            if not stack:
                required_removals += 1
            else:
                stack.pop()
        index += 1

    # TODO: Return the count of brackets that need to be removed to make the string valid
    required_removals += len(stack)
    return required_removals


# Example usage
invalid_parentheses = "()))(()"
removals_needed = min_removals_to_balance(invalid_parentheses)
print(removals_needed)  # Expected output: 3