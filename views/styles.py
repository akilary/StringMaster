from tkinter.ttk import Style
from views.theme import COLORS, FONT


def configure_styles():
    style = Style()
    style.theme_use("clam")
    style.configure("TFrame", background=COLORS["win_bg"])

    style.configure("TButton",
                    padding=7,
                    font=FONT["text"],
                    background=COLORS["btn_bg"],
                    foreground=COLORS["text_color"],
                    borderwidth=0)
    style.map("TButton",
              background=[("active", COLORS["btn_hover_bg"])])

    style.configure("TLabel",
                    padding=(10,0,10,0),
                    font=FONT["text"],
                    background=COLORS["win_bg"],
                    foreground=COLORS["text_color"])

    style.configure("TEntry",
                    fieldbackground=COLORS["editor_bg"],
                    foreground=COLORS["text_color"],
                    borderwidth=2,
                    padding=2,
                    insertcolor=COLORS["text_color"])
