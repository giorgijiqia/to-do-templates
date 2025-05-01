from flask import Flask, render_template, request, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'საიდუმლო_გასაღები'

users = {}

tasks = []

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', tasks=tasks, username=username)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            tasks.append(task)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_password = users.get(username)
        if user_password and check_password_hash(user_password, password):
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)