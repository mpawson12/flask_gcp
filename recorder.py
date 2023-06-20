import time
import cv2
import sounddevice as sd
import soundfile as sf

import static.config

current_file = "undefined"
recording_data = None
camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



def record_audio():
    global recording_data
    recording_data = sd.rec(int(static.config.sample_rate * static.config.duration),
                            samplerate=static.config.sample_rate,
                            channels=2,
                            blocking=False)


def save_audio():
    file_name = static.config.outfile_prefix + str(time.time()) + ".wav"
    sf.write(file_name,
             data=recording_data,
             samplerate=static.config.sample_rate)
    global current_file
    current_file = file_name
    print(f"written file {current_file}")
