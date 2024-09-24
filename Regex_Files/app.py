# app.py
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sample.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template('sample.html', matches=matched_strings)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$', email))
    return render_template('sample.html', email_valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)
