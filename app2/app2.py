from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

app = Flask(__name__)

# Khởi tạo Firebase Admin
cred = credentials.Certificate("./thoi-tiet-debe0-firebase-adminsdk-fbsvc-f4358b344f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route("/")
def index():
    # Chuyển hướng về trang hiển thị thời tiết
    return redirect(url_for("get_weathers"))

@app.route("/weathers", methods=["GET"])
def get_weathers():
    start_time = request.args.get("start")
    end_time = request.args.get("end")

    weathers_ref = db.collection("weathers")
    docs = weathers_ref.stream()

    weather_list = []
    for doc in docs:
        data = doc.to_dict()
        data['code'] = doc.id  # Thêm mã code từ document ID

        if start_time and end_time:
            try:
                t = datetime.fromisoformat(data["time"])
                start = datetime.fromisoformat(start_time)
                end = datetime.fromisoformat(end_time)
                if not (start <= t <= end):
                    continue
            except Exception:
                continue

        weather_list.append(data)

    return render_template("weathers.html", weathers=weather_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
