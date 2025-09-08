from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_on

def get_book_text():
    with open("books/frankenstein.txt", "r") as file:
        return file.read()
    


book_text = get_book_text()
get_number_of_words(book_text)
char_count = get_number_of_characters(book_text)

sorted_chars = sort_on(char_count)
for char, count in sorted_chars:
    print(f"'{char}': {count}")
