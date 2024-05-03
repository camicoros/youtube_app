import tkinter as tk
import pytube
from tkinter import messagebox, filedialog
from folder_operations import open_folder


class App():
    def __init__(self):
        self.bg_label_color = "#D3D3D3"

        # Заголовок формы
        self.root = tk.Tk()
        self.root.title("YouTube Video Downloader")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.root.config(bg=self.bg_label_color)

        lb = tk.Label(self.root, text="---Download video from YouTube---", font=("Arial,15,bold"), background=self.bg_label_color)
        lb.pack(pady=15)

        # Пояснительный текст для поля с адресом
        lb1 = tk.Label(self.root, text="Link to video: ", font=("Arial,15,bold"), background=self.bg_label_color)
        lb1.place(x=10, y=80)

        # Поле ввода адреса видео
        self.link_entry = tk.StringVar()
        en1 = tk.Entry(self.root, textvariable=self.link_entry, font=("Arial,15,bold"))
        en1.place(x=230, y=80)

        # Кнопка скачивания
        btn1 = tk.Button(self.root, text="Download", font=("Arial,10,bold"), bd=4, command=self.download)
        btn1.place(x=330, y=130)

        # Кнопки очистки и выхода
        btn2 = tk.Button(self.root, text="Reset", font=("Arial,10,bold"), bd=4, command=self.reset)
        btn2.place(x=160, y=190)
        btn3 = tk.Button(self.root, text="Exit", font=("Arial,10,bold"), bd=4, command=self.exit_program)
        btn3.place(x=250, y=190)

        # Путь до папки сохранения
        self.dir_path = "/"
        self.remember_dir = False
        self.dir_path_lb = tk.Label(self.root, text=f"Directory: {self.dir_path}", font=("Arial,15,bold"), background=self.bg_label_color)
        self.dir_path_lb.place(x=20, y=160)

        # Кнопка выбора папки для скачивания
        btn4 = tk.Button(self.root, text="Select Folder", font=("Arial,10,bold"), bd=4, command=self.ask_directory)
        btn4.place(x=20, y=190)

    def reset(self):
        # Очищаем строку с адресом видео
        self.link_entry.set("")

    def exit_program(self):
        # Закрываем окно с интерфейсом
        self.root.destroy()

    def download(self):
        """
        Берём адрес и с его помощью подключаемся к ютубу.
        Выясняем, какое у видео максимальное разрешение.
        Скачиваем это видео и сообщаем об этом пользователю.
        Если не получилось скачать видео по ссылке или получить
        данные о его качестве — выводим сообщение об ошибке.
        """

        if not self.remember_dir:
            self.ask_directory()

        try:
            # получаем адрес из формы
            youtube_link = self.link_entry.get()
            # создаём объект для взаимодействия с библиотекой pytube
            youtube_link_obj = pytube.YouTube(youtube_link)
            # запрашиваем у пользователя качество видео
            video_resolution = self.ask_video_resolution(youtube_link_obj)
            # получаем ссылку на видео с самым высоким качеством
            video = youtube_link_obj.streams.get_by_itag(int(str(video_resolution)))
            # скачиваем видео
            video.download(output_path=self.dir_path)
            # выводим результат
            messagebox.showinfo("Success", "Download complete")
            open_folder(self.dir_path)

        except Exception as exc:
            messagebox.showerror("Error", str(exc))

    def ask_video_resolution(self, youtube_obj):
        # TODO: разбить на функции
        title = youtube_obj.title
        streams_list = youtube_obj.streams

        get_better_quality = False
        if get_better_quality:
            audio_variants = ""
        else:
            video_variants = {stream.itag: f"{stream.mime_type}__{stream.resolution}__{stream.fps}fps__{stream.filesize_mb}Mb" for stream in streams_list.filter(progressive=True)}
            resolution_window = tk.Toplevel(self.root)
            resolution_window.title("Choose resolution")
            resolution_window.config(bg=self.bg_label_color)

            lb = tk.Label(resolution_window, text=f"Select resolution for {self.format_video_name(title)}", font=("Arial,15,bold"), background=self.bg_label_color)
            lb.place(x=100, y=40)

            resolution_itag = tk.StringVar(value=str(list(video_variants)[0]))
            row = 3
            for video_itag, video_description in video_variants.items():
                rad_b = tk.Radiobutton(
                    resolution_window, text=video_description, value=video_itag, variable=resolution_itag,
                    font=("Arial,15,bold"), background=self.bg_label_color)
                rad_b.place(x=100, y=row*40)
                row += 1

            # Кнопка скачивания
            btn = tk.Button(resolution_window, text="Choose resolution", font=("Arial,10,bold"), bd=4, command=lambda: resolution_window.destroy())
            btn.place(x=100, y=row*40)

            # подгоняем высоту окна
            resolution_window.geometry(f"600x{(row+3)*40}")
            self.root.resizable(False, False)

            # захватываем фокус
            resolution_window.transient(self.root)
            resolution_window.grab_set()
            self.root.wait_window(resolution_window)

        return resolution_itag.get()


    def ask_directory(self):
        """
        Спрашиваем директорию для скачивания, запоминаем её по выбору
        """

        self.dir_path = filedialog.askdirectory(initialdir=self.dir_path)
        self.remember_dir = messagebox.askyesno("", "Remember this directory?")
        self.dir_path_lb.config(text="Directory: {}".format(self.format_dir_name()))


    def format_dir_name(self):
        if len(self.dir_path) > 25:
            return f"...{self.dir_path[-25:]}"
        return self.dir_path

    @staticmethod
    def format_video_name(name):
        if len(name) > 25:
            return f"{name[:25]}..."
        return name


if __name__ == "__main__":
    app = App()
    # Запускаем окно
    app.root.mainloop()