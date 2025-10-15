# Complete the function to properly use stack operations for parenthesis matching
def is_valid_expression(expression):
    stack = []
    opening_paren = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            # TODO: Determine if the stack is empty OR the last character does not match the corresponding opening character
            if not stack:
                return False
            if stack[-1] == opening_paren[char]:
                stack.pop()
            else:
                return False
        # TODO: What to do if the `char` is not a parenthesis?

    # TODO: Check if the stack is empty, indicating that the expression is balanced
    if stack:
        return False
    return True  # Modify this line appropriately


# Example usage
sample_expression = "([a+b]{c+d})"
print(is_valid_expression(sample_expression))  # Expected output: True

bad_expression = "([a+b]{c+d}))"
print(is_valid_expression(bad_expression))  # Expected output: False