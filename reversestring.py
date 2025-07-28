def reverse_string(input_string):
    stack = list(input_string)

    reversed_string = ''
    while len(stack) > 0:
        reversed_string += stack.pop()
    return reversed_string


print(reverse_string('HELLO'))  # Outputs: OLLEH