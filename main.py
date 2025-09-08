def get_book_text():
    with open("books/frankenstein.txt", "r") as file:
        return file.read()
    
def get_number_of_words(text):
    words = text.split()
    print(len(words))

book_text = get_book_text()
get_number_of_words(book_text)