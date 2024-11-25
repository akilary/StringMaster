def remove_extra_spaces(text: str) -> str:
    """Удаляет лишние пробелы из текста."""
    return  " ".join(text.split())


def remove_all_spaces(text: str) -> str:
    """Удаляет все пробелы из текста."""
    return "".join(text.split())

def convert_to_uppercase(text: str) -> str:
    """Приводит текст к верхнему регистру."""
    return text.upper()


def convert_to_lowercase(text: str) -> str:
    """Приводит текст к нижнему регистру."""
    return text.lower()


def capitalize_words(text: str) -> str:
    """Делает каждое слово в тексте с заглавной буквы."""
    return text.title()

def capitalize_sentences(text: str) -> str:
    """Начинает каждое предложение с заглавной буквы."""
    sentences = text.split(". ")
    return ". ".join(sentence.capitalize() for sentence in sentences)

def reverse_text(text: str) -> str:
    """Разворачивает текст."""
    return " ".join(reversed(text.split()))


def reverse_letters(text: str) -> str:
    """Разворачивает буквы в тексте."""
    return text[::-1]


def search_and_replace(text: str, old: str, new: str) -> str:
    """Ищет и заменяет строку."""
    return text.replace(old, new)
