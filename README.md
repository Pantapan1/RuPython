# RuPython — Русский Python

Пиши код на Python полностью на русском языке. Транспилятор автоматически переводит русский синтаксис в стандартный Python и запускает код.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Pantapan1/RuPython/blob/main/LICENSE)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.4.0-orange.svg)](https://github.com/Pantapan1/RuPython)

---

## 📦 Установка

```bash
pip install https://github.com/Pantapan1/RuPython/archive/main.zip

# привет.rpy
функция приветствие(имя, возраст):
    если возраст < 18:
        печать(f"Привет, {имя}! Ты ещё молод.")
    или_если возраст < 60:
        печать(f"Здравствуйте, {имя}!")
    иначе:
        печать(f"Моё почтение, {имя}!")

имя = ввод("Ваше имя: ")
возраст = целое(ввод("Ваш возраст: "))
приветствие(имя, возраст)

ruspy привет.rpy -o привет.py && python3 привет.py
