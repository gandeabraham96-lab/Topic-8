def shout(text):
    return text.upper() + "!"


def word_count(text):
    return len(text.split())

from string_utils import shout, word_count

sentence = input("Enter a sentence: ")

print("Shouted:", shout(sentence))
print("Word count:", word_count(sentence))