def count_words(text):
    return len(text.split())

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    if text.lower() == reverse_text(text).lower():
        return True
    else:
        return False

def capitalize_sentence(text):
    return text.title()

# TEST CASES
print(count_words("Hello, I like programming!"))
print(reverse_text("Hello, I like programming!"))
print(is_palindrome("Hello, I like programming!"))
print(is_palindrome("racecar"))
print(capitalize_sentence("Hello, I like programming!"))