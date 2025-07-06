from stats import count_words
from stats import count_letters
from stats import listed_letters
import sys
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
def sort_let(item):
    return item["num"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    letter_count = listed_letters(count_letters(text))
    letter_count.sort(reverse=True, key=sort_let)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key in range(0, len(letter_count)):
        char = letter_count[key]["char"]
        num = letter_count[key]["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
main()

