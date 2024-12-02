import tkinter.messagebox as mb


def check_empty_text(func):
    """Декоратор для проверки пустого текста."""

    def wrapper(*args: str):
        text = args[0]
        if text == "":
            mb.showinfo("Предупреждение", "Поле для ввода текста пустое")
            return ""
        return func(*args)

    return wrapper


def validate_search_and_replace(func):
    """Декоратор для проверки корректности операции поиска и замены текста."""

    def wrapper(*args: str):
        try:
            text, old, new = args
            if old not in text:
                mb.showinfo("Ошибка замены текста", f"Символ '{old}' не найден")
                return text
        except ValueError:
            mb.showinfo("Ошибка замены текста", f"Одно из полей пустое")
            return args[0]

        return func(*args)

    return wrapper
