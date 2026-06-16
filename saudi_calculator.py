#!/usr/bin/env python3
"""
🇸🇦 Al-Hassib (الحاسب) — The Funky Saudi Calculator 🇸🇦

A simple GUI calculator dressed in Saudi green and gold, with palm-tree
flair, Arabic-Indic numerals, and a few salams sprinkled in.

Run it with:  python3 saudi_calculator.py
(requires Tkinter, which ships with most Python installs)
"""

import tkinter as tk
from tkinter import font as tkfont

# --- Saudi-inspired palette -------------------------------------------------
SAUDI_GREEN = "#006C35"   # the green of the flag
DEEP_GREEN = "#004d25"    # darker shade for depth
DESERT_GOLD = "#C9A227"   # sand & gold accents
SAND = "#F4E9CD"          # warm display background
WHITE = "#FFFFFF"
NIGHT = "#062b1a"         # deep oasis-night background

# Map Western digits to Arabic-Indic numerals for a funky touch on the display
ARABIC_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")


class SaudiCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🇸🇦 Al-Hassib — الحاسب")
        self.root.configure(bg=NIGHT)
        self.root.resizable(False, False)

        self.expression = ""

        self._build_header()
        self._build_display()
        self._build_buttons()
        self._build_footer()

    # -- UI sections ---------------------------------------------------------
    def _build_header(self):
        header = tk.Label(
            self.root,
            text="🌴  الحاسب السعودي  🐪",
            font=("Helvetica", 18, "bold"),
            bg=NIGHT,
            fg=DESERT_GOLD,
            pady=10,
        )
        header.grid(row=0, column=0, columnspan=4, sticky="nsew")

    def _build_display(self):
        self.display_var = tk.StringVar(value="٠")
        display = tk.Label(
            self.root,
            textvariable=self.display_var,
            anchor="e",
            font=("Courier New", 30, "bold"),
            bg=SAND,
            fg=DEEP_GREEN,
            width=12,
            padx=15,
            pady=20,
            relief="ridge",
            bd=6,
        )
        display.grid(row=1, column=0, columnspan=4, padx=12, pady=(0, 12), sticky="nsew")

    def _build_buttons(self):
        # (label, row, col, kind)
        buttons = [
            ("C", 2, 0, "clear"), ("⌫", 2, 1, "clear"), ("%", 2, 2, "op"), ("÷", 2, 3, "op"),
            ("7", 3, 0, "num"), ("8", 3, 1, "num"), ("9", 3, 2, "num"), ("×", 3, 3, "op"),
            ("4", 4, 0, "num"), ("5", 4, 1, "num"), ("6", 4, 2, "num"), ("−", 4, 3, "op"),
            ("1", 5, 0, "num"), ("2", 5, 1, "num"), ("3", 5, 2, "num"), ("+", 5, 3, "op"),
            ("0", 6, 0, "num"), (".", 6, 1, "num"), ("🐪", 6, 2, "easter"), ("=", 6, 3, "equals"),
        ]

        styles = {
            "num":    dict(bg=WHITE, fg=DEEP_GREEN, activebackground=SAND),
            "op":     dict(bg=SAUDI_GREEN, fg=WHITE, activebackground=DEEP_GREEN),
            "clear":  dict(bg=DESERT_GOLD, fg=NIGHT, activebackground="#b08e1f"),
            "equals": dict(bg=DESERT_GOLD, fg=NIGHT, activebackground="#b08e1f"),
            "easter": dict(bg=DEEP_GREEN, fg=DESERT_GOLD, activebackground=SAUDI_GREEN),
        }

        btn_font = tkfont.Font(family="Helvetica", size=18, weight="bold")

        for (label, r, c, kind) in buttons:
            style = styles[kind]
            btn = tk.Button(
                self.root,
                text=label,
                font=btn_font,
                width=4,
                height=1,
                bd=0,
                relief="flat",
                cursor="hand2",
                command=lambda l=label: self.on_press(l),
                **style,
            )
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

    def _build_footer(self):
        footer = tk.Label(
            self.root,
            text="صُنع بكل حب  •  Made with 💚 in the Kingdom",
            font=("Helvetica", 10, "italic"),
            bg=NIGHT,
            fg=SAND,
            pady=8,
        )
        footer.grid(row=7, column=0, columnspan=4, sticky="nsew")

    # -- Behaviour -----------------------------------------------------------
    def on_press(self, label):
        if label == "C":
            self.expression = ""
        elif label == "⌫":
            self.expression = self.expression[:-1]
        elif label == "=":
            self._evaluate()
            return
        elif label == "🐪":
            self.display_var.set("أهلاً وسهلاً 🐪")
            return
        else:
            # Convert pretty operator glyphs to Python operators internally
            self.expression += {"×": "*", "÷": "/", "−": "-"}.get(label, label)

        self._refresh_display()

    def _evaluate(self):
        try:
            # Guard the eval to arithmetic-only characters
            allowed = set("0123456789+-*/%. ")
            if not self.expression or set(self.expression) - allowed:
                raise ValueError
            result = eval(self.expression)  # noqa: S307 - input is sanitised above
            # Tidy whole numbers (3.0 -> 3)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("لا تقسم على صفر! 🚫")
            self.expression = ""
            return
        except Exception:
            self.display_var.set("خطأ — Error 😅")
            self.expression = ""
            return
        self._refresh_display()

    def _refresh_display(self):
        if not self.expression:
            self.display_var.set("٠")
            return
        # Show pretty operators and Arabic-Indic digits on screen
        pretty = (
            self.expression
            .replace("*", " × ")
            .replace("/", " ÷ ")
            .replace("-", " − ")
            .replace("+", " + ")
        )
        self.display_var.set(pretty.translate(ARABIC_DIGITS))


def main():
    root = tk.Tk()
    SaudiCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
