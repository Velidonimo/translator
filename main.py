"""
A simple program to translate a word from english to russian
and save the history of translates in a database

"""
import tkinter as tk
import json
import backend as be


def translate():
    """Translate a word"""
    rus.var.set(be.translate(engl.var.get()))


def run():
    """Runs the program"""
    label_input = tk.Label(root, text=data['labels']['input'], font=data['window_params']['font_size'])
    label_input.grid(row=0, column=1)

    global engl, rus
    engl = Lang('engl', 1)
    rus = Lang('rus', 2)

    btn = tk.Button(root, text=data['translate'], font=data['window_params']['font_size'], command=translate)
    btn.grid(row=3, column=1)


class Lang:
    """
    Class of language representation in the window
    lang: language (string)
    row: a row of language in the window
    """
    def __init__(self, lang, row):
        self.label = tk.Label(root, text=data['lang']['lang_name'][lang], font=data['window_params']['font_size'])
        self.label.grid(row=row, column=0)
        self.var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.var, width=data['window_params']['entry_width'])
        self.entry.grid(row=row, column=1)
        self.var.set(data['lang']['lang_popup'][lang])

        self.entry.bind('<Return>', lambda event: translate())


if __name__ == '__main__':
    with open('data.json', encoding='utf-8') as file:
        data = json.load(file)
    root = tk.Tk()
    run()
    root.mainloop()
