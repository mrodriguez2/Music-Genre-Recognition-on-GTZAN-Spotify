import os
from pydub import AudioSegment

def process_wav(song, tag):
    i = 0
    to_return = []
    
    total_duration = len(AudioSegment.from_wav(song))
    
    intervals =  int(total_duration / 3000)
    
    for w in range(0, intervals):
        i = i + 1
        t1 = 3 * (w) * 1000
        t2 = 3 * (w + 1) * 1000
        newAudio = AudioSegment.from_wav(song)
        new = newAudio[t1:t2]
        new.export(str(tag) + '_' + str(w) + '.wav', format = "wav")
        to_return.append(str(w) + '.wav')
        
    return to_return, intervals

path = "country_more/"

#Change working directory
os.chdir(path)

audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
i = 0
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".wav":
       process_wav(file, i)
       i += 1