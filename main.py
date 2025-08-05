from stats import get_word_count, character_count, sort_by_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #char_dict.sort()
    #print(char_dict)
    char_list = sort_by_count(char_dict)
    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()