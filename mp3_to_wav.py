import os
from pydub import AudioSegment

path = "country_more/"

#Change working directory
os.chdir(path)

audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       sound = AudioSegment.from_mp3(file)
       sound = sound.set_channels(1)
       sound = sound.set_frame_rate(22050)
       #rename them using the old name + ".wav"
       sound.export("{0}.wav".format(name), format = "wav")