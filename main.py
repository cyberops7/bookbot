#!/usr/bin/env python3

import sys

from stats import get_character_count, get_word_count, sort_character_counts


def get_book_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    
    num_words = get_word_count(book_text)
    print(f"Found {num_words} total words")

    char_count = get_character_count(book_text)
    print(char_count)

    sorted_char_count = sort_character_counts(char_count)
    for item in sorted_char_count:
        if type(item["char"]) == str and item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


if __name__ == "__main__":
    main()
