import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash

# Khởi tạo Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Kết nối Firebase
cred = credentials.Certificate("./thoi-tiet-debe0-firebase-adminsdk-fbsvc-f4358b344f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Giao diện chính với tìm kiếm
@app.route('/')
def index():
    keyword = request.args.get('q', '').lower()
    weathers = db.collection('weathers').stream()
    weather_list = []
    for w in weathers:
        data = w.to_dict()
        data['code'] = w.id
        if keyword in data['code'].lower() or keyword in data['name'].lower():
            weather_list.append(data)
        elif not keyword:
            weather_list.append(data)
    return render_template('index.html', weathers=weather_list, keyword=keyword)

# Thêm
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        time = request.form['time']
        temperature = request.form['temperature']
        humidity = request.form['humidity']
        wind = request.form['wind']
        pressure = request.form['pressure']

        if not code or not name or not time or not temperature or not humidity or not wind or not pressure:
            flash('Vui lòng nhập đủ thông tin!', 'error')
            return redirect(url_for('add'))

        db.collection('weathers').document(code).set({
            'name': name,
            'time': time,
            'temperature': temperature,
            'humidity': humidity,
            'wind': wind,
            'pressure': pressure
        })
        flash('Thêm thông tin thành công!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html')

# Sửa 
@app.route('/edit/<code>', methods=['GET', 'POST'])
def edit(code):
    weather_doc = db.collection('weathers').document(code).get()
    if not weather_doc.exists:
        flash('Thông tin thời tiết không tồn tại!', 'error')
        return redirect(url_for('index'))

    weather = weather_doc.to_dict()
    weather['code'] = code

    if request.method == 'POST':
        name = request.form['name']
        time = request.form['time']
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        wind = float(request.form['wind'])
        pressure = float(request.form['pressure'])

        db.collection('weathers').document(code).update({
            'name': name,
            'time': time,
            'temperature': temperature,
            'humidity': humidity,
            'wind': wind,
            'pressure': pressure
        })
        flash('Cập nhật thành công!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html', weather=weather)

# Xóa
@app.route('/delete/<code>', methods=['POST'])
def delete(code):
    db.collection('weathers').document(code).delete()
    flash('Xóa thành công!', 'success')
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


