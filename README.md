## CS767 - Music Genre Recognition using CNNs on GTZAN + Spotify

The goal of this project is to be able to **detect the genre of a song by training a Convolutional Neural Network (CNN)**.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Spectrogram-19thC.png/400px-Spectrogram-19thC.png" />
</p>

To do this, we will use the GTZAN dataset which consists of 900 **30-second, 22kHz, Mono, 16-bit .WAV files**, belonging to 9 different genres from **2000-2001**:



* Blues
* Pop
* Rock
* Classical
* Country
* Disco
* Hiphop
* Metal
* Reggae

As 100 samples per class is a very small sample size, we will split the 30-second clips into 10 3-second clips each, making it 1000 samples per class.

Once we have this, we will generate the image representation of a song, also known as a **mel spectrogram**, which covers all the main characteristics that represent sound. The idea is that our CNN will be able to detect patterns in these spectrograms that allow it to differentiate between genres.

We will use this base dataset to find the optimal neural network structure. From there on, we will amplify the dataset with more songs from those same genres and create new genres using Spotify, and compare the results.

In particular, the two genres that we will include will be ‘Rap’ and ‘Brazilian Funk’. ‘Rap’ because it is one of the biggest music genres out there and it would be interesting to build a genre from scratch using Spotify and see how it performs versus the original GTZAN dataset.

**Brazilian Funk** for two purposes: first and foremost, it is a wink to my **sweet Brazilian life partner, Sofia**. Secondly, it is a genre that is usually used to remix popular songs and it will be an interesting observation to compare our model with the original song vs the remixed, Brazilian Funk, version of the song. The inspiration behind this was **Rihanna’s Brazilian Funk interpretation of her hit ‘Rude Boy’ at this year’s Super Bowl**.

Most importantly however, we hope to use this project as a learning opportunity to improve our knowledge on Machine Learning, Artificial Intelligence and Neural Networks.
