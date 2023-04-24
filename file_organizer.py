import os
from pydub import AudioSegment
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from multiprocessing import Pool
import time
import math
import shutil


genres = 'blues classical country disco pop hiphop metal reggae rock'
genres = genres.split()

'''
i = 0
for g in genres:
  j=0
  print(g)
  for filename in os.listdir(os.path.join("genres_original", g)):

    song  =  os.path.join("genres_original", g, filename)
    j = j+1
    for w in range(0,10):
      i = i+1
      #print(i)
      t1 = 3*(w)*1000
      t2 = 3*(w+1)*1000
      newAudio = AudioSegment.from_wav(song)
      new = newAudio[t1:t2]
      new.export(f'files/{g+str(j)+str(w)}.wav', format="wav")
'''


def generate_spectogram_for_g(g):
  j = 0
  print(g)
  for filename in os.listdir("files"):
    if filename.endswith(".wav") and g in filename:
      start_time = time.time()
      song  =  os.path.join("files", filename)
      j = j+1

      x, sr = librosa.load(song, sr = None)
      X = librosa.stft(x)
      Xdb = librosa.amplitude_to_db(abs(X))
      librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
      plt.axis('off')

      #check if song file exists
      if os.path.isfile(filename.replace(".wav", ".jpg")):
        continue
      else:
        print("saved {}".format(filename))
        plt.savefig(os.path.join("files", filename.replace(".wav", ".jpg")), bbox_inches='tight')
        plt.cla()
        print("--- %s seconds ---" % (time.time() - start_time))


#for g in genres:
temp_list = []
for filename in os.listdir("country_more"):
  if filename.endswith(".jpg"):
    temp_list.append(filename)
#randomly shuffle elements in temp_list
np.random.shuffle(temp_list)
#get first 100 elements of temp_list
validation = temp_list[:900]
#get the next 100 elements of temp_list
testing = temp_list[900:1800]
#get the rest elements of temp_list
training = temp_list[1800:]
for image in validation:
  #move file from files to validation folder
  shutil.move(os.path.join("country_more", image), os.path.join("original_dataset_country", "validation", "country", image))
for image in testing:
  shutil.move(os.path.join("country_more", image), os.path.join("original_dataset_country", "testing", "country", image))
for image in training:
  shutil.move(os.path.join("country_more", image), os.path.join("original_dataset_country", "training", "country", image))

'''
for g in genres:
  for filename in os.listdir("files/testing/"):
    if filename.endswith(".jpg") and g in filename:
      shutil.move(os.path.join("files", 'testing', filename), os.path.join("files", "testing", g, filename))
'''