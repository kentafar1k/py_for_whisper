# 🎤 Whisper Interview Transcriber

Python-скрипт для расшифровки аудиозаписей собеседований в текст с помощью модели Whisper от OpenAI.  
Подходит для использования на **macOS** и **Windows**.

---

## 📌 Возможности

- Поддержка форматов `.m4a`, `.mp3`, `.wav`
- Распознавание **русского и английского** языка
- Простота установки
- Помогает анализировать собеседования, выявлять слабые/сильные стороны и расти как специалисту

---

## 💻 Установка

### macOS

```bash
# Установите Homebrew (если не установлен)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установите ffmpeg
brew install ffmpeg

# Установите зависимости проекта
python3 -m pip install -r requirements.txt
```

---

### Windows

```bash
:: 1. Установите Python 3.9+
:: 2. Скачайте ffmpeg:
:: https://www.gyan.dev/ffmpeg/builds/

:: 3. Распакуйте и добавьте путь к ffmpeg.exe в системную переменную PATH

:: 4. Установите зависимости:
python -m pip install -r requirements.txt
```

---

## 🚀 Использование

1. Переименуйте вашу аудиозапись в `interview.m4a`
2. Поместите её в корень проекта рядом с `transcribe.py`
3. Запустите скрипт:

```bash
python3 transcribe.py
```

4. Результат появится в файле `result.txt` в той же папке

---

## 📝 Пример результата

```
Интервьюер: Расскажите, пожалуйста, о вашем опыте.
Я: Меня зовут Артём, я работаю QA-инженером уже более трёх лет. Начинал как мануальщик...
...
```

---

## 📁 Структура проекта

```
voice-to-text-sobes/
├── transcribe.py          # Основной скрипт
├── requirements.txt       # Зависимости
├── README.md              # Документация
├── interview.m4a          # Входной файл (аудио)
└── result.txt             # Выходной файл (текст)
```

---

## 👤 Автор

Артём Кривошеин  


---

## 📄 Лицензия

MIT License
