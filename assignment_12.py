#function definition

def is_palindrome(word):
    word = word.casefold()
    if word == word[::-1]:
        return True
    else:
        return False

#user input

word = input('\nenter word: ').strip()

#function call

output = is_palindrome(word)
print('\nGiven word palindrome?')
print(output)
