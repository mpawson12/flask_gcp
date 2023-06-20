import time
import sounddevice as sd
import soundfile as sf
import static.config

recording_data = None


def record_audio():
    global recording_data

    print("start recording")
    recording_data = sd.rec(int(static.config.sample_rate * static.config.duration),
                            samplerate=static.config.sample_rate,
                            channels=2,
                            blocking=True)
    print("stopped recording")


def save_audio():
    sf.write(static.config.outfile_prefix + str(time.time()) + ".wav",
             data=recording_data,
             samplerate=static.config.sample_rate)
