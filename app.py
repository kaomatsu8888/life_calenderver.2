from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)


# ユーザーに生年月日を入力させるためのルート
@app.route("/", methods=["GET"])
def input_birthdate():
    return render_template("input_birthdate.html")


# ユーザーからの入力を受け取り、ライフカレンダーを表示するルート
@app.route("/calendar", methods=["POST"])
def calendar():
    # ユーザーからの入力を取得
    year = int(request.form.get("year"))
    month = int(request.form.get("month"))
    day = int(request.form.get("day"))
    birth_date = datetime(year, month, day)

    # 仮の死亡日を計算（例：生後84年後）
    death_date = birth_date + timedelta(days=84 * 365)

    # 以下は既存の計算コード
    now = datetime.now()
    total_days = (death_date - birth_date).days
    passed_days = (now - birth_date).days
    left_days = total_days - passed_days
    total_years = int(total_days / 365)
    total_weeks = int(total_days / 7)
    passed_weeks = int(passed_days / 7)
    left_weeks = int(left_days / 7)

    return render_template(
        "index.html",
        birth_date=birth_date.strftime("%B %d, %Y"),
        death_date=death_date.strftime("%B %d, %Y"),
        total_years=total_years,
        now=now.strftime("%B %d, %Y"),
        total_days=total_days,
        passed_days=passed_days,
        left_days=left_days,
        total_weeks=total_weeks,
        passed_weeks=passed_weeks,
        left_weeks=left_weeks,
    )


if __name__ == "__main__":
    app.run(debug=True)
