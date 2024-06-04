from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "user1@example.com": {"password": "password1"},
    "user2@example.com": {"password": "password2"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users and users[email]['password'] == password:
            # Authentication successful
            return redirect(url_for('dashboard'))
        else:
             return render_template('login.html', message='Invalid email or password. Please try again.')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email not in users:
            # Add new user to the database
            users[email] = {"password": password}
            return redirect(url_for('login'))
        else:
            return render_template('register.html', message='User already exists. Please login.')

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    # Logic for logging out the user (e.g., clearing session)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)