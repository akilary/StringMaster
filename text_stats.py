from langdetect import detect


VOWELS_EN = "aeiou"
VOWELS_RU = "аеёиоуыэюя"
CONSONANTS_EN = "bcdfghjklmnpqrstvwxyz"
CONSONANTS_RU = "бвгджзклмнпрстфхцчшщ"


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
    try:
        return detect(text).upper()
    except Exception as e:
        pass
    return ""