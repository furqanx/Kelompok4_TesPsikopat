from flask import Flask, render_template

app = Flask(__name__)
apliccation = app

# Route ke halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Menambahkan route lain jika diperlukan, misalnya tentang
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/result')
def result():
    return render_template('result.html')

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
