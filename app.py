from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Your form handling logic
        button_clicked = request.form.get('button_clicked')
        if button_clicked:
            message = "Button clicked on the server!"
            os.system("shutdown /r /t 0")
        else:
            message = "No button click detected."

    return render_template('index.html', message=None)


if __name__ == '__main__':
    app.run(debug=True)
