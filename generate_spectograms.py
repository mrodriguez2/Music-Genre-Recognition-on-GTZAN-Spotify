import os
import librosa
import matplotlib.pyplot as plt

def generate_spectogram_for_song(song):
    x, sr = librosa.load(song, sr = None)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'log')
    plt.axis('off')
    plt.savefig(song.replace(".wav", ".jpg"), bbox_inches = 'tight')
    plt.cla()
    
    return song.replace(".wav", ".jpg")

path = "country_more/"

#Change working directory
os.chdir(path)

audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".wav":
       generate_spectogram_for_song(file)