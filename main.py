from tkinter import Tk
from tkinter.ttk import Frame, Button, Label, Entry
from typing import Callable

from views.editor import Editor
from views.styles import configure_styles
from views.theme import COLORS, FONT
from text_utils.text_operations import *
from text_utils.text_stats import *


class StringMaster:
    def __init__(self, root: Tk):
        self.root = root

        self.root.title("String-Master")
        self.root.resizable(False, False)

        self.root.configure(background=COLORS["win_bg"])
        configure_styles()

        self.editor = Editor(self.root)
        self.editor.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="we")

        self._create_text_actions_panel()
        self._create_search_replace_panel()
        self._create_text_controls_panel()
        self.stats_labels = self._create_stats_panel()

        self.root.after(250, self.update_stats_periodically)

    def _create_text_actions_panel(self) -> None:
        """Создаёт панель с кнопками для выполнения различных операций над текстом."""
        frame = Frame(self.root)
        frame.grid(row=1, column=0, rowspan=2, padx=10, pady=5, sticky="w")

        (Button(frame, text="Удалить повторяющиеся пробелы", command=lambda: self.update_text(remove_extra_spaces))
         .grid(row=0, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Удалить все пробелы из текста", command=lambda: self.update_text(remove_all_spaces))
         .grid(row=0, column=1, padx=5, pady=5, sticky="ew"))

        (Button(frame, text="Привести текст к верхнему регистру", command=lambda: self.update_text(convert_to_uppercase))
         .grid(row=1, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Привести текст к нижнему регистру", command=lambda: self.update_text(convert_to_lowercase))
         .grid(row=1, column=1, padx=5, pady=5, sticky="ew"))

        (Button(frame, text="Сделать каждое слово с заглавной буквы", command=lambda: self.update_text(capitalize_words))
         .grid(row=2, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Начать каждое предложение с заглавной буквы", command=lambda: self.update_text(capitalize_sentences))
         .grid(row=2, column=1, padx=5, pady=5, sticky="ew"))

        (Button(frame, text="Развернуть текст", command=lambda: self.update_text(reverse_text))
         .grid(row=3, column=0, padx=5, pady=5, sticky="we"))

        (Button(frame, text="Развернуть буквы", command=lambda: self.update_text(reverse_letters))
         .grid(row=3, column=1, padx=5, pady=5, sticky="ew"))


    def _create_search_replace_panel(self) -> None:
        """Создаёт панель для поиска и замены текста."""
        frame = Frame(self.root)
        frame.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="we")

        Label(frame, text="Найти :").grid(row=0, column=0, padx=5, pady=5, sticky="w")

        old_text = Entry(frame, width=16, font=FONT["text"])
        old_text.grid(row=0, column=1, padx=5, sticky="w")

        Label(frame, text="Заменить на :").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        new_text = Entry(frame, width=16, font=FONT["text"])
        new_text.grid(row=1, column=1, padx=5)

        (Button(frame, text="Применить",  command=lambda: self.update_text(search_and_replace, old_text.get(), new_text.get()))
         .grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we"))

    def _create_text_controls_panel(self) -> None:
        """Создаёт панель с элементами управления текстом."""
        frame = Frame(self.root)
        frame.grid(row=2, column=1, padx=10, pady=5, sticky="wes")

        (Button(frame, text="Копировать текст", command=lambda: copy_text(self.editor))
         .grid(row=0, column=0, padx=5, pady=5))

        (Button(frame, text="Удалить текст", command=lambda: clear_text(self.editor))
         .grid(row=0, column=1, padx=5, pady=5))

    def _create_stats_panel(self) -> tuple[Label, Label, Label, Label, Label, Label]:
        """Создаёт панель с элементами управления текстом."""
        frame = Frame(self.root)
        frame.grid(row=3, column=0, padx=10, columnspan=2, pady=5, sticky="w")

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
        text = self.editor.get(1.0, "end-1c")

        vowels, consonants = calculate_vowel_and_consonant_count(text)
        self.stats_labels[0].config(text=f"Гласных: {vowels}")
        self.stats_labels[1].config(text=f"Согласных: {consonants}")
        self.stats_labels[2].config(text=f"Палиндром: {"Да" if is_palindrome(text) else "Нет"}")
        self.stats_labels[3].config(text=f"Всего слов: {word_count(text)}")
        self.stats_labels[4].config(text=f"Всего символов: {letter_count(text)}")
        self.stats_labels[5].config(text=f"Раскладка: {detected_text(text)}")

        self.root.after(1000, self.update_stats_periodically, )


    def update_text(self, operation: Callable, old_text: str = None, new_text: str = None) -> None:
        """Применяет указанную операцию к тексту редактора."""
        text = self.editor.get(1.0, "end-1c")

        if old_text and new_text:
            self.editor.replace("1.0", "end", operation(text, old_text, new_text))
        else:
            self.editor.replace("1.0", "end", operation(text))


if __name__ == '__main__':
    win = Tk()
    StringMaster(win)
    win.mainloop()
