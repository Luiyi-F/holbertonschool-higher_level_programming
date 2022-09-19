#!/usr/bin/python3
word = "Holberton"
word_first_3 = f"{word[:3]}"    # take only 3 first letters
word_last_2 = f"{word[-2:]}"    # take only 2 last letters
middle_word = f"{word[1:-1]}"   # take only middle letters
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
