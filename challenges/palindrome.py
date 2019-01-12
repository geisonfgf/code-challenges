"""
Given a string, write a python function to check if it is palindrome or not.
A string is said to be palindrome if reverse of the string is same as string.
For example, “radar” is palindrome, but “radix” is not palindrome.

Input = radar
Expected result = True
"""

def is_palindrome_using_for(text):
    for i in range(0, int(round(len(text)/2))):
        if text[i] != text[len(text)-i-1]:
            return False
    return True

def is_palindrome_using_while(text):
    left_index = 0
    right_index = len(text)-1
    while left_index < right_index:
        if text[left_index] != text[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

def is_palindrome_using_reversed_string(text):
    if (text == text[::-1]):
        return True
    return False

if __name__ == '__main__':
    print()
    print("is_palindrome_using_for")
    print("Input radar")
    print("Expected result: ", True)
    print("Result: ", is_palindrome_using_for("radar"))

    print()

    print("is_palindrome_using_for")
    print("Input radix")
    print("Expected result: False")
    print("Result: ", is_palindrome_using_for("radix"))

    print()
    print("==================================")
    print()

    print("is_palindrome_using_while")
    print("Input radar")
    print("Expected result: ", True)
    print("Result: ", is_palindrome_using_while("radar"))

    print()

    print("is_palindrome_using_while")
    print("Input radix")
    print("Expected result: False")
    print("Result: ", is_palindrome_using_while("radix"))

    print()
    print("==================================")
    print()

    print("is_palindrome_using_reversed_string")
    print("Input radar")
    print("Expected result: ", True)
    print("Result: ", is_palindrome_using_reversed_string("radar"))

    print()

    print("is_palindrome_using_reversed_string")
    print("Input radix")
    print("Expected result: False")
    print("Result: ", is_palindrome_using_reversed_string("radix"))
