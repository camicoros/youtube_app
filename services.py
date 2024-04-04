import pytube
from tkinter import messagebox, filedialog
from functools import wraps


def ask_directory_decorator(func):
    memoize_dict = {"remember_dir": False}

    @wraps(func)
    def wrapper(*args, **kwargs):
        directory, remember_ans = ask_directory(remember_directory=memoize_dict.get("remember_dir"))
        func(*args, **kwargs, directory=directory)
        memoize_dict.update({"remember_dir": remember_ans})

    return wrapper


def reset(link_obj):
    # Очищаем строку с адресом видео
    link_obj.set("")


def exit_program(root_obj):
    # Закрываем окно с интерфейсом
    root_obj.destroy()


@ask_directory_decorator
def download(link, directory="/"):
    """
    Берём адрес и с его помощью подключаемся к ютубу.
    Выясняем, какое у видео максимальное разрешение.
    Скачиваем это видео и сообщаем об этом пользователю.
    Если не получилось скачать видео по ссылке или получить
    данные о его качестве — выводим сообщение об ошибке.
    """

    try:
        # формируем адрес
        youtube_link = link.get()
        # переводи в нужный формат
        youtube_link_obj = pytube.YouTube(youtube_link)
        # получаем ссылку на видео с самым высоким качеством
        video = youtube_link_obj.streams.get_highest_resolution()
        # скачиваем видео
        video.download(output_path=directory)
        # выводим результат
        messagebox.showinfo("Success", "Download complete")
    except Exception as exc:
        messagebox.showerror("Error", str(exc))


def ask_directory(old_directory="/", remember_directory=False):
    """
    Спрашиваем директорию для скачивания, запоминаем её по выбору
    :param old_directory:
    :param remember_directory:
    :return:
    """
    if remember_directory:
        return old_directory, remember_directory

    directory = filedialog.askdirectory(initialdir=old_directory)
    remember_directory = messagebox.askyesno("", "Remember this directory?")

    return directory, remember_directory


