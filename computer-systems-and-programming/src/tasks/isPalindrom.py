def check_if_string_is_palindrome(word):
    first = 0
    last = len(word) - 1

    while first <= last:
        if word[first] != word[last]:
            return False
        first += 1
        last -= 1

    return True

# Example usage
input_word = "madam"
result = check_if_string_is_palindrome(input_word)
print(f"Is '{input_word}' a palindrome? {result}")
