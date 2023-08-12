import os
import shutil
from pytube import YouTube
import moviepy.editor as mp


"""
Если выходит ошибка >>> pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W 
Чтобы решить проблему, вы должны зайти в файл cipher.py и заменить строку 30, а именно:
    var_regex = re.compile(r"^\w+\W")
    на эту строку ниже
    var_regex = re.compile(r"^\$*\w+\W")
    Источник: StackOverflow
"""

link = "https://www.youtube.com/watch?v=1rC9Wh4-RfQ"

print("Load")
yt = YouTube(link).streams.get_audio_only().download()
print("End Loading")
# print(mp)











