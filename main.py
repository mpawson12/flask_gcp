from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('landing.html')


@app.route('/recorder', methods=['GET', 'POST'])
def recorder():
    button_state = "Start Recording"
    if request.method == 'POST':
        print(request.form['recording_button'])
        if request.form['recording_button'] == 'start':
            print("start_record trigger event")
            button_state = "Stop Recording"
        elif request.form['recording_button'] == 'stop':
            print("stop_record trigger event")
    return render_template('recorder.html', button_state=button_state)


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
