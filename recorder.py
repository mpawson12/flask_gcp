import time
import wave
from multiprocessing import Process

import pyaudio
import numpy as np
import sounddevice as sd
import soundfile as sf
import static.config

recording_data = None

def record_audio():
    global recording_data

    recording_data = sd.rec(int(static.config.sample_rate * static.config.duration),
                            samplerate=static.config.sample_rate,
                            channels=2,
                            blocking=True)
sf.write(static.config.outfile_prefix + str(time.time()) + ".wav",
         data=recording_data,
         samplerate=static.config.sample_rate)

"""do_record = False
audio = None
stream = None
frames = []
process = None


def save_recording():
    print("save triggered")
    global stream
    global audio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    for i in range(len(frames)):
        chunk = np.fromstring(frames[i], np.int16)
        chunk *= 2
        frames[i] = chunk.astype(np.int16)

    file = wave.open("recording.wav", "wb")
    file.setnchannels(1)
    file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    file.setframerate(44100)
    file.writeframes(b''.join(frames))


# cant do threads in the real thing as single user only
# would use celery for the task management instead
def record_loop():
    global do_record
    print("record_loop called")
    while do_record:
        print("loop alive")
        global frames
        data = stream.read(1024)
        frames.append(data)


def start_record():
    global stream
    global audio
    global do_record
    global process
    do_record = True
    print("started")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    process = Process(target=record_loop())
    process.start()


def stop_record():
    global do_record
    do_record = False
    print("stopped")
    save_recording()"""
