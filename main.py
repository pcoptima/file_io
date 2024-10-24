from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb
import pyperclip
import os
import json


file_save = 'history_link.json'


def save_history(file_save, link, file):
    history = []
    if os.path.exists(file_save):
        with open(file_save, 'r') as f:
            history = json.load(f)
    history.append({'name_file': os.path.basename(file),
                    'link': link,
                    'save_file': os.path.basename(file_save)})
    with open(file_save, 'w') as f:
        json.dump(history, f, indent=4)


def get_response():
    try:
        file = fd.askopenfilename()
        if file:
            with open(file, 'rb') as fi:
                f = {'file': fi}
                answer_json = requests.post('https://file.io', files=f)
                if answer_json.status_code == 200:
                    link = answer_json.json()['link']
                    e.delete(0, END)
                    e.insert(0, link)
                    pyperclip.copy(link)
                    save_history(file_save, link, file)

    except Exception as exc:
        mb.showerror('Ошибка', message=f'Произошла ошибка: {exc}')


window = Tk()
window.title('Отправка файлов в file.io')
window.geometry(f'400x300+{window.winfo_screenwidth() //
                2-200}+{window.winfo_screenheight()//2-150}')

btn = ttk.Button(window, text='Выбрать файл', command=get_response)
btn.pack(pady=10)

e = Entry(window, width=30, font=("arial", 14))
e.pack(pady=10)

window.mainloop()
