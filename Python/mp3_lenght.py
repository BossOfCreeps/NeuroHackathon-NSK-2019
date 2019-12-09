from mutagen.mp3 import MP3

filename = "good.mp3"

audio = MP3(filename)

print (audio.info.length)
