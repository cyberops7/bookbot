#!/usr/bin/env python3

import sys

from stats import chars_dict_to_sorted_list, get_character_count, get_word_count

# from stats import get_character_count, get_word_count, sort_character_counts


def get_book_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents


def print_report(book_path: str, num_words: int, sorted_chars: list[tuple[str, int]]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    # Original hardcoded fallback — replaced by the required CLI argument above.
    # book_path = sys.argv[1] if len(sys.argv) > 1 else "books/frankenstein.txt"

    book_text = get_book_text(book_path)
    
    num_words = get_word_count(book_text)
    # print(f"Found {num_words} total words")

    char_count = get_character_count(book_text)
    # print(char_count)

    sorted_chars = chars_dict_to_sorted_list(char_count)
    # print(sorted_chars)

    print_report(book_path, num_words, sorted_chars)


if __name__ == "__main__":
    main()
