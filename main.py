from flask import Flask, render_template, request

import static.config
from recorder import record_audio, save_audio
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
            record_audio()
            # do other processing here
            save_audio()
            # redirect to playback

    return render_template('recorder.html',
                           button_state=button_state,
                           speaking_time=static.config.duration)


@app.route('/confirm')
def confirm_recording():

    return render_template('confirm.html')


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
