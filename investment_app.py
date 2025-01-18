from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

# Загрузка обученных моделей
with open("kmeans_model.pkl", "rb") as f:
    kmeans_model = pickle.load(f)

with open("risk_model.pkl", "rb") as f:
    risk_model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = request.form["investment"]
            investment_data = np.array([float(x) for x in data.split(",")]).reshape(-1, 1)

            # Кластеризация
            clusters = kmeans_model.predict(investment_data)
            risks = risk_model.predict(investment_data)

            # Подготовка данных для визуализации
            chart_data = {
                "amounts": investment_data.flatten().tolist(),
                "clusters": clusters.tolist(),
                "risks": risks.tolist()
            }
            return jsonify(chart_data)
        except ValueError:
            return "Ошибка: Введите данные в виде чисел, разделенных запятыми.", 400
    return render_template("investment.html")

if __name__ == "__main__":
    app.run(debug=True)
