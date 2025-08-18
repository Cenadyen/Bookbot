from stats import get_num_words, char_count, char_list, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()

def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(file_path)
    num_words = get_num_words(book)
    character_dictionary = char_count(book)
    sorted_char_list = char_list(character_dictionary)
    sorted_char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
     
main()