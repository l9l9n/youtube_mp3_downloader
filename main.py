import os
from pytube import YouTube

"""
Если выходит ошибка >>> pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W 
Чтобы решить проблему, вы должны зайти в файл cipher.py и заменить строку 30, а именно:
    var_regex = re.compile(r"^\w+\W")
    на эту строку ниже
    var_regex = re.compile(r"^\$*\w+\W")
    Источник: StackOverflow
"""


def download_mp3(link):
    """Функция для загрузки, только mp3 формата"""
    # Обьект yt получает ссылку link
    yt = YouTube(link)

    # Здесь фильтруется файл """only_audio=True"""
    video = yt.streams.filter(only_audio=True).first()

    # Здесь можете указать путь или папку для загрузки файла
    print('Куда хотите сохранить файл?\nНажмите Enter и файл сохранится в текущей директории!')
    destination = input(">> ") or '.'
    # Загрузка самого файла
    print("----- Loading -----")
    out_of_file = video.download(output_path=destination)
    # Здесь мы отделяем название от mp4 и заменяем ее на mp3
    base, extend = os.path.splitext(out_of_file)
    new_file = base + '.mp3'
    os.rename(out_of_file, new_file)
    print("--- End loading ---")


link = input("Введите ссылку: ")

if __name__ == '__main__':
    print("--- Start ---")
    download_mp3(link)










