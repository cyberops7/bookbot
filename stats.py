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


def sort_character_counts(counts: dict[str, int]) -> list[dict[str, int | str]]:
    sorted_counts: list[dict[str, int | str]] = [
        {"char": k, "num": v} for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)
    ]
    
    return sorted_counts
