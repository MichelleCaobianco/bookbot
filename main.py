import sys
from stats import get_number_of_words
from stats import get_number_of_characters
from stats import sort_on


def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)    

book_path = sys.argv[1] 
book_text = get_book_text(book_path)

print("Menu:")
print("1 - Book Info")
print("2 - Read Book")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    get_number_of_words(book_text)
    print("-------- Character Count --------")
    sorted_chars = sort_on(get_number_of_characters(book_text))
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
elif choice == "2":
    print("\n-------- Book Content --------")
    print(book_text)
else:
    print("Invalid choice. Please enter 1 or 2.")