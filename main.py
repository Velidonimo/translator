import tkinter as tk
import json


def run():
    label_input = tk.Label(root, text=data['labels']['input'])
    label_input.grid(row=0, column=1)

    engl = Lang('engl', 1)
    rus = Lang('rus', 2)

    btn = tk.Button(root, text=data['translate'])
    btn.grid(row=3, column=1)


class Lang:
    def __init__(self, lang, row):
        self.label = tk.Label(root, text=data['lang']['lang_name'][lang])
        self.label.grid(row=row, column=0)
        self.var = tk.StringVar()
        self.entry = tk.Entry(root, text=self.var)
        self.entry.grid(row=row, column=1)
        self.var.text = data['lang']['lang_popup'][lang]


if __name__ == '__main__':
    with open('languages.json') as file:
        data = json.load(file, encoding='UTF-8')
    root = tk.Tk()
    run()
    root.mainloop()
