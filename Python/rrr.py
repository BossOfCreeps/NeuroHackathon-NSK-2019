from pydub import AudioSegment
from pydub.playback import play

from pygame import mixer 
from mutagen.mp3 import MP3

#AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffmpeg = "C:\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffprobe ="C:\\ffmpeg\\bin\\ffprobe.exe"


def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

sound = AudioSegment.from_file("good.mp3", format="mp3")

slow_sound = speed_change(sound, 1/1.3)
#fast_sound = speed_change(sound, 2.0)

slow_sound.export('new.mp3', format='mp3')


mixer.init()
mixer.music.load('new.mp3')
mixer.music.play()
