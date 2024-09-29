from flask import Flask, render_template, request, redirect, flash, url_for
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answers = {
        'q1': int(request.form.get('q1') or 0), 'q2': int(request.form.get('q2') or 0), 'q3': int(request.form.get('q3') or 0), 'q4': int(request.form.get('q4') or 0),
        'q5': int(request.form.get('q5') or 0), 'q6': int(request.form.get('q6') or 0), 'q7': int(request.form.get('q7') or 0), 'q8': int(request.form.get('q8') or 0),
        'q9': int(request.form.get('q9') or 0), 'q10': int(request.form.get('q10') or 0), 'q11': int(request.form.get('q11') or 0), 'q12': int(request.form.get('q12') or 0),
        'q13': int(request.form.get('q13') or 0), 'q14': int(request.form.get('q14') or 0), 'q15': int(request.form.get('q15') or 0), 'q16': int(request.form.get('q16') or 0),
        'q17': int(request.form.get('q17') or 0), 'q18': int(request.form.get('q18') or 0), 'q19': int(request.form.get('q19') or 0),'q20': int(request.form.get('q20') or 0)
    }

    total = sum(answers.values())

    # menambahkan rule
    if 80 <= total <= 100:
        status_psikopat =  "Anda Psikopat Ekstrim"
    elif 60 <= total <= 79:
        status_psikopat =  "Anda Psikopat Tinggi"
    elif 40 <= total <= 59:
        status_psikopat =  "Anda Psikopat Sedang"
    elif 20 <= total <= 39:
        status_psikopat =  "Anda Psikopat Rendah"
    else:
        status_psikopat =  "Anda Tidak Menunjukkan Tanda-tanda Psikopat"

    return render_template('result.html', answers=answers, total=total, status_psikopat=status_psikopat)


