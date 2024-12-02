from tkinter import Text
from views.theme import COLORS, FONT


class Editor(Text):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            wrap="word",
            width=50, height=13,
            background=COLORS["editor_bg"],
            foreground=COLORS["text_color"],
            borderwidth=4,
            font=FONT["entry_text"],
            padx=10, pady=10,
            insertbackground=COLORS["text_color"],
            insertofftime=250,
            insertontime=250,
            undo=True,
            selectbackground=COLORS["text_color"],
            selectforeground=COLORS["editor_bg"])
