from stats import get_word_count, character_count

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(text)
    char_dict = character_count(text)
    print(f"{num_words} words found in the document")
    print(char_dict)

main()