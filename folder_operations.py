import os
import platform


def open_folder_windows(folder_name: str):
    os.system('explorer "%s"' % folder_name)


def open_folder_osx(folder_name: str):
    os.system('open "%s"' % folder_name)


def open_folder_linux(folder_name: str):
    os.system('xdg-open "%s"' % folder_name)


def open_folder(folder_name: str):
    PlATFORMS = {
        "linux": open_folder_linux,
        "darwin": open_folder_osx,
        "windows": open_folder_windows,
    }

    platform_name = str(platform.system()).lower()
    try:
        PlATFORMS[platform_name](folder_name)
    except KeyError:
        print(f"Can't open folder in system {platform_name}")


if __name__ == "__main__":
    open_folder("C:\\Users\\dd.saushkin\\Downloads")