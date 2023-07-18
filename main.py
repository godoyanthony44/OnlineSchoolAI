from flask import Flask, url_for, redirect, request, render_template
from flask_bootstrap import Bootstrap5
from classe.claudehandler import Claude
from classe.undetecable import Undetectable

chat = Claude()
chat2 = Undetectable()

def send_message(message):
    message = chat.send_chat_message(message)
    message = chat2.send_message(message)
    return message


app = Flask(__name__)
Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')



@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/response')
def response():
    text = request.args.get('text')
    return render_template('response.html', text=text)


@app.route('/submit', methods=['GET','POST'])
def submit():
    text_input = request.form.get('textfield')  # Get the text input value
    data = send_message(text_input)
    return redirect(url_for('response', text=data))


if __name__ == '__main__':

    app.run()
