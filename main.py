from flask import Flask, render_template, request, redirect, send_from_directory

import static.config
from recorder import record_audio, save_audio
app = Flask(__name__)

current_file = "undefined"


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
            # do other processing here ie video
            global current_file
            current_file = save_audio()
            # redirect to playback and confirmation
            return redirect("confirm", code=301)

    return render_template('recorder.html',
                           button_state=button_state,
                           speaking_time=static.config.duration)


@app.route('/audio/<path:filename>')
def get_audio(filename):
    return send_from_directory(
        "D:\\flask_gcp",
        filename,
        as_attachment=True,
        mimetype='audio/wav'
    )


@app.route('/confirm', methods=['GET', 'POST'])
def confirm_recording():
    if request.method == "POST":
        if request.form.get("redo") == "redo":
            return redirect("recorder", code=301)
        elif request.form.get("submit") == "submit":
            ...
            # upload
            return redirect("loading", code=301)
    return render_template('confirm.html', audio_file=current_file)

@app.route('/loading', methods=['GET'])
def loading():
    return render_template('loading.html')


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
