import tensorflow as tf
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Список знаков зодиака и их даты
ZODIAC_SIGNS = [
    ("Овен", (3, 21), (4, 19)),
    ("Телец", (4, 20), (5, 20)),
    ("Близнецы", (5, 21), (6, 20)),
    ("Рак", (6, 21), (7, 22)),
    ("Лев", (7, 23), (8, 22)),
    ("Дева", (8, 23), (9, 22)),
    ("Весы", (9, 23), (10, 22)),
    ("Скорпион", (10, 23), (11, 21)),
    ("Стрелец", (11, 22), (12, 21)),
    ("Козерог", (12, 22), (1, 19)),
    ("Водолей", (1, 20), (2, 18)),
    ("Рыбы", (2, 19), (3, 20)),
]

# Функция определения знака зодиака
def get_zodiac_sign(day, month):
    for sign, (start_month, start_day), (end_month, end_day) in ZODIAC_SIGNS:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            birthdate = request.form["birthdate"]
            year, month, day = map(int, birthdate.split("-"))
            sign = get_zodiac_sign(day, month)
            if not sign:
                return render_template("zodiac.html", result="Ошибка: Невозможно определить знак зодиака.")
            return render_template("zodiac.html", result=f"Ваш знак зодиака: {sign}")
        except ValueError:
            return render_template("zodiac.html", result="Ошибка: Введите корректную дату.")
    return render_template("zodiac.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
