from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/mypage/me')
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')

        print("\n--------- NOWA WIADOMOŚĆ ---------")
        print(f"\n{message}\n")
        print("----------------------------------\n")

    return render_template('contact.html')
