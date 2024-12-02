VOWELS_EN = "aeiou"
VOWELS_RU = "аеёиоуыэюя"
CONSONANTS_EN = "bcdfghjklmnpqrstvwxyz"
CONSONANTS_RU = "бвгджзклмнпрстфхцчшщ"
RU_ALPHABET = VOWELS_RU + CONSONANTS_RU
EN_ALPHABET = VOWELS_EN + CONSONANTS_EN


def calculate_vowel_and_consonant_count(text: str) -> tuple[int, int]:
    """Считает количество гласных и согласных."""
    vowels = sum([1 for char in text.lower() if char in VOWELS_RU + VOWELS_EN])
    consonants = sum([1 for char in text.lower() if char in CONSONANTS_RU + CONSONANTS_EN])
    return vowels, consonants


def is_palindrome(text: str) -> bool:
    """Проверяет, является ли текст палиндромом."""
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]


def word_count(text: str) -> int:
    """Считает количество слов в тексте."""
    return len(text.split())


def letter_count(text: str) -> int:
    """Считает количество символов в тексте."""
    return len(text)


def detected_text(text: str) -> str:
    """Определяет раскладку клавиатуры."""
    ru_count = sum([1 for let in text.lower() if let in RU_ALPHABET])
    en_count = sum([1 for let in text.lower() if let in EN_ALPHABET])

    if ru_count > en_count:
        return "Кир."
    elif en_count > ru_count:
        return "Лат."
    return "?"
