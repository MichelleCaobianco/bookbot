def get_number_of_words(text):
    words = text.split()
    print(len(words),"words found in the document")

def get_number_of_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)  # <-- Move this line up  
    return char_count
    
def sort_on(char_count):
    return sorted(char_count.items(), key=lambda item: item[1], reverse=True)