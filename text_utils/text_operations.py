try:
    import pyperclip
except ImportError:
    print("Please install pyperclip")
    pyperclip = None
from tkinter import Text
from typing import Literal

from helpers.decorators import *


def format_text_lines(
        text: str,
        operation: Literal["remove_extra_spaces", "remove_all_spaces", "reverse_text", "reverse_letters"]
    ) -> list[str]:
    """Форматирует текст в соответствии с заданной операцией."""
    formated_text = []
    for line in text.splitlines():
        match operation:
            case "remove_extra_spaces":
                formated_text.append(" ".join(line.split()))
            case "remove_all_spaces":
                formated_text.append("".join(line.split()))
            case "reverse_text":
                formated_text.append(" ".join(reversed(line.split())))
            case "reverse_letters":
                formated_text.append(" ".join(word[::-1] for word in line.split()))
    return formated_text


@check_empty_text
def remove_extra_spaces(text: str) -> str:
    """Удаляет лишние пробелы из текста."""
    formated_text = format_text_lines(text, "remove_extra_spaces")
    return "\n".join(formated_text)


@check_empty_text
def remove_all_spaces(text: str) -> str:
    """Удаляет все пробелы из текста."""
    formated_text = format_text_lines(text, "remove_all_spaces")
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
    formated_text = format_text_lines(text, "reverse_text")
    return "\n".join(formated_text)


@check_empty_text
def reverse_letters(text: str) -> str:
    """Разворачивает буквы в тексте."""
    formated_text = format_text_lines(text, "reverse_letters")
    return "\n".join(formated_text)


@check_empty_text
@validate_search_and_replace
def search_and_replace(text: str, old: str, new: str) -> str:
    """Ищет и заменяет строку."""
    return text.replace(old, new)


def clear_text(editor: Text) -> None:
    """Удаляет весь текст из редактора."""
    editor.delete(1.0, "end")


def copy_text(editor: Text) -> None:
    """Копирует весь текст в буфер обмена."""
    if pyperclip is None:
        print("Копирование текста недоступно. Установите модуль 'pyperclip' для этой функции.")
        return
    text = editor.get("1.0", "end-1c")
    pyperclip.copy(text) # type: ignore
