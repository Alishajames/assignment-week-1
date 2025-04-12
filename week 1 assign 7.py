#Write a program, to replace – all vowel , with “x” of word in this story.
string = "My name is alisha."
vowels = "aeiou"

new_string = ''
for char in string:
    if char.lower() in vowels:
        new_string += 'x'  
    else:
        new_string += char 

print("Original String:", string)
print("New String:", new_string)


#Write a program, to replace “He” with “She” , “What” with “Who”, “a” with “The” , “On” with “at” of word in this story. Print it.

story="""He is a boy, what are you doing on this place"""
n_story=story.lower()
n_story=n_story.replace("he","she")
n_story=n_story.replace("what","who")
n_story=n_story.replace("a","the")
n_story=n_story.replace("on","at")

print(n_story)




