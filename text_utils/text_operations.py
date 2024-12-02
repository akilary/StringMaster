from tkinter import Text
from pyperclip import copy
from typing import Literal

from helpers.decorators import *


def get_format_text(text: str,
                    operation: Literal["remove_extra", "remove_all", "reverse_text", "reverse_letters"]) -> list[str]:
    formated_text = []
    for line in text.splitlines():
        if operation == "remove_extra":
            formated_text.append(" ".join(line.split()))
        elif operation == "remove_all":
            formated_text.append("".join(line.split()))
        elif operation == "reverse_text":
            formated_text.append(" ".join(reversed(line.split())))
        elif operation == "reverse_letters":
            formated_text.append(" ".join(word[::-1] for word in line.split()))
    return formated_text


@check_empty_text
def remove_extra_spaces(text: str) -> str:
    """Удаляет лишние пробелы из текста."""
    formated_text = get_format_text(text, "remove_extra")
    return "\n".join(formated_text)


@check_empty_text
def remove_all_spaces(text: str) -> str:
    """Удаляет все пробелы из текста."""
    formated_text = get_format_text(text, "remove_all")
    return "\n".join(formated_text)


@check_empty_text
def convert_to_uppercase(text: str) -> str:
    """Приводит текст к верхнему регистру."""
    return text.upper()


@check_empty_text
def convert_to_lowercase(text: str) -> str:
    """Приводит текст к нижнему регистру."""
    return text.lower()


@check_empty_text
def capitalize_words(text: str) -> str:
    """Делает каждое слово в тексте с заглавной буквы."""
    return text.title()


@check_empty_text
def capitalize_sentences(text: str) -> str:
    """Начинает каждое предложение с заглавной буквы."""
    sentences = text.split(". ")
    return ". ".join(sentence.capitalize() for sentence in sentences)


@check_empty_text
def reverse_text(text: str) -> str:
    """Разворачивает текст."""
    formated_text = get_format_text(text, "reverse_text")
    return "\n".join(formated_text)


@check_empty_text
def reverse_letters(text: str) -> str:
    """Разворачивает буквы в тексте."""
    formated_text = get_format_text(text, "reverse_letters")
    return "\n".join(formated_text)


@check_empty_text
@validate_search_and_replace
def search_and_replace(text: str, old: str, new: str) -> str:
    """Ищет и заменяет строку."""
    return text.lower().replace(old, new)


def clear_text(editor: Text) -> None:
    """Удаляет весь текст из редактора."""
    editor.delete(1.0, "end")


def copy_text(editor: Text) -> None:
    """Копирует весь текст в буфер обмена."""
    text = editor.get("1.0", "end-1c")
    copy(text)
