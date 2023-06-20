import time
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


def save_audio():
    file_name = static.config.outfile_prefix + str(time.time()) + ".wav"
    sf.write(file_name,
             data=recording_data,
             samplerate=static.config.sample_rate)
    return file_name
