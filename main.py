from tkinter import *
import requests
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox as mb


def get_response():
    file = fd.askopenfilename()
    if file:
        f = {'file': open(file, 'rb')}
        answer_json = requests.post('https://file.io', files=f)
        if answer_json.status_code == 200:
            link = answer_json.json()['link']
            e.insert(0, link)


window = Tk()
window.title('Отправка файлов в file.io')
window.geometry(f'400x300+{window.winfo_screenwidth() //
                2-200}+{window.winfo_screenheight()//2-150}')

btn = ttk.Button(window, text='Выбрать файл', command=get_response)
btn.pack(pady=10)

e = Entry(window, width=30, font=("arial", 14))
e.pack(pady=10)

window.mainloop()
