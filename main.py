def get_book_text():
    with open("books/frankenstein.txt", "r") as file:
        return file.read()
    
print(get_book_text())