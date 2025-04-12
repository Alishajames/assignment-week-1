def has_vowel(word):
    vowels = "aeiou"
    for char in word.lower():
        if char in vowels:
            return True
    return False

def list_words_with_vowels(sentence):
    words = sentence.split()
    words_with_vowels = [word for word in words if has_vowel(word)]
    return words_with_vowels

# Input from the user
user_input = input("Enter a string: ")

# Get words with vowels
words_with_vowels = list_words_with_vowels(user_input)
print("Words with vowels:", words_with_vowels)