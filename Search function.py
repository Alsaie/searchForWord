#Search function
text = input("Please enter your text: ")
word = input("Please enter a word: ")

def search(text, word,):
    if word in text:
        return "Word found"
    else:
        return "Word not found"

print(search(text, word))