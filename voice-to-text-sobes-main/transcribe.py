import whisper
import os


# явное указание пути в path
os.environ['PATH'] = r"E:\PROGRAMS\ffmpeg\ffmpeg-2025-08-25-git-1b62f9d3ae-essentials_build\bin;" + os.environ['PATH']

model = whisper.load_model("small")  # можно заменить на "small" или "large" или как было "medium"
result = model.transcribe("interview.m4a", language="ru")

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Готово! Результат сохранён в result.txt")


# запустить: python transcribe.py
