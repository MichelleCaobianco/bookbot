from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_on

def get_book_text():
    with open("books/frankenstein.txt", "r") as file:
        return file.read()
    

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
book_text = get_book_text()
get_number_of_words(book_text)
print("-------- Character Count --------")
sorted_chars = sort_on(get_number_of_characters(book_text))

for char, count in sorted_chars:
    if char.isalpha():
        print(f"{char}:{count}")