from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Khởi tạo Firebase Admin
cred = credentials.Certificate("./thoi-tiet-debe0-firebase-adminsdk-fbsvc-f4358b344f.json")  # đường dẫn đến file JSON bạn tải về
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        code = request.form['code']
        doc_ref = db.collection('weathers').document(code)
        doc = doc_ref.get()
        if doc.exists:
            weather = {
                "code": doc.id,   # Thêm tên document (code)
                **doc.to_dict()   # Thêm toàn bộ dữ liệu bên trong
            }
        else:
            weather = {"error": "Không tìm thấy thời tiết"}
    return render_template('search.html', weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
