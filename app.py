from flask import Flask, render_template, request

app = Flask(__name__)

results_db = {
    "325531": {
        "reg": "1310384293/2019-20",
        "exam": "HSC",
        "year": "2021",
        "board": "Dhaka",
        "documents": [
            {"title": "HSC Academic Certificate", "file": "certificate.png"},
            {"title": "HSC Academic Marksheet", "file": "marksheet.png"}
        ]
    },
    "387889": {
        "reg": "1610597071/2016",
        "exam": "JSC",
        "year": "2016",
        "board": "Dhaka",
        "documents": [
            {"title": "JSC Academic Certificate", "file": "jsc_certificate.png"},
            {"title": "JSC Academic Marksheet", "file": "jsc_marksheet.png"}
        ]
    },
    "325532": {
        "reg": "1310384294/2019-20",
        "exam": "HSC",
        "year": "2021",
        "board": "Dhaka",
        "documents": [
            {"title": "HSC Academic Certificate", "file": "certificate_anzuman.png"},
            {"title": "HSC Academic Marksheet", "file": "marksheet_anzuman.png"}
        ]
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        roll = request.form.get('roll', '').strip()
        reg = request.form.get('reg', '').strip()
    else:
        roll = request.args.get('roll', '').strip()
        reg = request.args.get('reg', '').strip()
    
    documents = None
    exam = ""
    year = ""
    board = ""
    
    # শুধু রোল নম্বর ডাটাবেজে থাকলেই সার্টিফিকেট শো করবে (রেজিস্ট্রেশন নম্বর কন্ডিশন তুলে দেওয়া হয়েছে)
    if roll in results_db:
        student_data = results_db[roll]
        documents = student_data["documents"]
        exam = student_data["exam"]
        year = student_data["year"]
        board = student_data["board"]

    return render_template('result.html', roll=roll, reg=reg, exam=exam, year=year, board=board, documents=documents)

if __name__ == '__main__':
    app.run(debug=True)
