from tkinter import Tk, Text
from tkinter.ttk import Frame, Style, Button, Label, Entry
from typing import Callable

from text_operations import *
from text_stats import *


class StringMaster:
    def __init__(self, root: Tk):
        self.root = root

        self.root.resizable(False, False)

        self.root.configure(background="#DCDAD5")
        style = Style()
        style.theme_use("clam")

        self.editor_text = Text(self.root, height=15, wrap="word")
        self.editor_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self.root.after(1000, self.update_stats_periodically)

        self._create_text_actions_panel()
        self._create_search_replace_panel()
        self._create_text_controls_panel()
        self.stats_labels = self._create_stats_panel()

    def _create_text_actions_panel(self) -> None:
        frame = Frame(self.root)
        frame.grid(row=1, column=0, rowspan=2, padx=10, pady=5)

        (Button(frame, text="Удалить повторяющиеся пробелы", command=lambda: self.update_text(remove_extra_spaces))
         .grid(row=0, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Удалить все пробелы из текста", command=lambda: self.update_text(remove_all_spaces))
         .grid(row=0, column=1, padx=5, pady=5, sticky="ew"))

        (Button(frame, text="Привести текст к верхнему регистру", command=lambda: self.update_text(convert_to_uppercase))
         .grid(row=1, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Привести текст к нижнему регистру", command=lambda: self.update_text(convert_to_lowercase))
         .grid(row=1, column=1, padx=5, pady=5, sticky="ew"))

        (Button(frame, text="Сделать каждое слово с заглавной буквы", command=lambda: self.update_text(capitalize_words))
         .grid(row=2, column=0, padx=5, pady=5, sticky="w"))

        (Button(frame, text="Начать каждое предложение с заглавной буквы", command=lambda: self.update_text(capitalize_sentences))
         .grid(row=2, column=1, padx=5, pady=5, sticky="ew"))

    def _create_search_replace_panel(self) -> None:
        frame = Frame(self.root)
        frame.grid(row=1, column=1, padx=10, pady=5)

        Label(frame, text="Найти :").grid(row=0, column=0, padx=5, pady=5)

        old_text = Entry(frame, width=15)
        old_text.grid(row=0, column=1, padx=5)

        Label(frame, text="заменить на :").grid(row=0, column=2, padx=5, pady=5)
        new_text = Entry(frame, width=15)
        new_text.grid(row=0, column=3, padx=5)

        (Button(frame, text="Применить", command=lambda: self.update_text(search_and_replace, old_text.get(), new_text.get()))
         .grid(row=1, column=0, columnspan=4, padx=5, pady=5))

    def _create_text_controls_panel(self) -> None:
        reverse_text_frame = Frame(self.root)
        reverse_text_frame.grid(row=2, column=1, padx=10, pady=5, sticky="wes")

        (Button(reverse_text_frame, text="Развернуть текст", command=lambda: self.update_text(reverse_text))
         .grid(row=0, column=0, padx=5, pady=5))

        (Button(reverse_text_frame, text="Развернуть буквы", command=lambda: self.update_text(reverse_letters))
         .grid(row=0, column=1, padx=5, pady=5))

        (Button(reverse_text_frame, text="Удалить текст", command=self.clear_text)
         .grid(row=0, column=2, padx=5, pady=5))

    def _create_stats_panel(self) -> tuple[Label, Label, Label, Label, Label, Label]:
        frame = Frame(self.root)
        frame.grid(row=3, column=0, padx=10, columnspan=2, pady=5)

        vowels = Label(frame, text="Гласных: 0")
        vowels.grid(row=0, column=0, padx=5, pady=5)

        consonants = Label(frame, text="Согласных: ")
        consonants.grid(row=0, column=1, padx=5, pady=5)

        palindrome = Label(frame, text="Палиндром: ")
        palindrome.grid(row=0, column=2, padx=5, pady=5)

        total_words = Label(frame, text="Всего слов: ")
        total_words.grid(row=0, column=3, padx=5, pady=5)

        total_letters = Label(frame, text="Всего символов: ")
        total_letters.grid(row=0, column=4, padx=5, pady=5)

        layout = Label(frame, text="Раскладка: ")
        layout.grid(row=0, column=5, padx=5, pady=5)
        return vowels, consonants, palindrome, total_words, total_letters, layout

    def update_stats_periodically(self):
        """Периодически обновляет статистику текста, основываясь на содержимом редактора."""
        text = self.editor_text.get(1.0, "end-1c")

        vowels, consonants = calculate_vowel_and_consonant_count(text)
        self.stats_labels[0].config(text=f"Гласных: {vowels}")
        self.stats_labels[1].config(text=f"Согласных: {consonants}")

        self.stats_labels[2].config(text=f"Палиндром: {"Да" if is_palindrome(text) else "Нет"}")

        self.stats_labels[3].config(text=f"Всего слов: {word_count(text)}")

        self.stats_labels[4].config(text=f"Всего символов: {letter_count(text)}")

        self.stats_labels[5].config(text=f"Раскладка: {detected_text(text)}")

        self.root.after(1000, self.update_stats_periodically)

    def clear_text(self) -> None:
        """Удаляет весь текст из редактора."""
        self.editor_text.delete(1.0, "end")

    def update_text(self, operation: Callable, old_text: str=None, new_text: str=None) -> None:
        """Применяет указанную операцию к тексту редактора."""
        text = self.editor_text.get(1.0, "end-1c")
        if old_text and new_text:
            self.editor_text.replace("1.0", "end", operation(text, old_text, new_text))
        else:
            self.editor_text.replace("1.0", "end", operation(text))


if __name__ == '__main__':
    win = Tk()
    StringMaster(win)
    win.mainloop()
