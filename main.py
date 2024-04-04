import tkinter as tk

from services import download, reset, exit_program


# Заголовок формы
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("450x250")

lb = tk.Label(root, text="---Download video from YouTube---", font=("Arial,15,bold"), background="#D3D3D3")
lb.pack(pady=15)

# Пояснительный текст для поля с адресом
lb1 = tk.Label(root, text="Link to video: ", font=("Arial,15,bold"), background="#D3D3D3")
lb1.place(x=10, y=80)

# Поле ввода адреса видео
link1 = tk.StringVar()
En1 = tk.Entry(root, textvariable=link1, font=("Arial,15,bold"))
En1.place(x=230, y=80)

# Кнопка скачивания
btn1 = tk.Button(root, text="Download", font=("Arial,10,bold"), bd=4, command=lambda: download(link1))
btn1.place(x=330, y=130)

# Кнопки очистки и выхода
btn2 = tk.Button(root, text="Reset", font=("Arial,10,bold"), bd=4, command=lambda: reset(link1))
btn2.place(x=160, y=190)
btn3 = tk.Button(root, text="Exit", font=("Arial,10,bold"), bd=4, command=lambda: exit_program(root))
btn3.place(x=250, y=190)

# Запускаем окно
root.mainloop()