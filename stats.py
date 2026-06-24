def get_character_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    text_lower = text.lower()

    for char in text_lower:
        if counts.get(char):
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def get_word_count(text: str) -> int:
    return len(text.split())


def sort_on(t: tuple[str, int]) -> int:
    return t[1]


def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    char_list: list[tuple[str, int]] = []
    for char in counts:
        char_list.append((char, counts[char]))
    return sorted(char_list, key=sort_on, reverse=True)
