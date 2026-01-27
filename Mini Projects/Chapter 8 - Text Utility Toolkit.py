def count_words(text):
    return len(text.split())

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    if text.lower() == reverse_text(text).lower():
        return True
    else:
        return False

def reverse_capitlization(text):
    final_text = ""
    for letter in text:
        if letter.isupper():
            final_text += letter.lower()
        else:
            final_text += letter.upper()
    return final_text




# TEST CASES
print(count_words("Hello, I like programming!"))
print(reverse_text("Hello, I like programming!"))
print(is_palindrome("Hello, I like programming!"))
print(is_palindrome("racecar"))
print(reverse_capitlization("Hello, I like programming!"))