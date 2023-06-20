from threading import Thread

from flask import Flask, render_template, request, redirect, send_from_directory, Response
from google.cloud import storage

import static.config
from recorder import record_audio, save_audio, gen_frames
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('landing.html')


@app.route('/record_audio', methods=['POST'])
def record_audio_router():
    print("record router call")
    return Response(record_audio())


@app.route('/save_audio', methods=['POST'])
def save_audio_router():
    print("save audio call")
    return Response(save_audio())


@app.route('/recorder', methods=['GET'])
def recorder():
    """if request.method == 'POST':
        if request.form['recording_button'] == 'start':
            thread = Thread(record_audio())
            thread.start()
            thread.join(10)
            # do other processing here ie video
            global current_file
            current_file = save_audio()
            # redirect to playback and confirmation
            return redirect("confirm", code=301)
    else:"""
    return render_template('recorder.html',
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
    from recorder import current_file
    if request.method == "POST":
        print(current_file)
        if request.form.get("redo") == "redo":
            return redirect("recorder", code=301)
        elif request.form.get("submit") == "submit":

            bucket_name = "inc-data-stb"
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(current_file)
            blob.upload_from_filename(current_file)


            return redirect("loading", code=301)
    return render_template('confirm.html', audio_file=current_file)


@app.route('/loading', methods=['GET'])
def loading():
    return render_template('loading.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
