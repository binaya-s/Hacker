# Multi-target Voice Conversion without Parallel Data by Adversarially Learning Disentangled Audio Representations

## IIT Bombay CS-753 Automatic Speech Recognition : Hacker Implementation

### Team Name : Overload.ai
### Team Members : 
- Nihar Mahesh Gupte (213070002)
- Araveeti Sai Pavan (213070007)
- Binaya Kumar Sahoo (213070009)

This is the implementation of the paper on a smaller subset of the dataset : VCTK Corpus, with 8 speakers, compared to 
the original paper implementation at [Original Github Link](https://github.com/jjery2243542/voice_conversion).

The github link mentioned here also uses the content of the tacotron model implementation by the same author as a part of
preprocessing steps.

# Dependencies
- python 3.6+
- pytorch 0.4.0
- h5py 2.8
- tensorboardX

To run the code, in order to take care of the computational power, we are using Google Colab as the shell, and running 
all the '.py' files in form of commands on Google Colaboratory notebook. The link for the same is provided [here](https://colab.research.google.com/drive/12IX6mbH6nsMVlVpfmQBBK53H0tu9bCad?usp=sharing).
The instructions are mentioned in the colab notebook itself to run the code.

# Dataset Link
The link to download the subset of the dataset is [here](https://drive.google.com/uc?id=1GOM281Ah4WTjBsO2eJpJ--TTqExgjDc1&export=download) 

# Changes to Original Work
- The original dataset contains 109 speakers with 400 wav files each, so we took a smaller subset of the original dataset 
with 8 speakers each. 
- We used 50,000 samples (segments of 128 sample length) in place of 5,00,000 samples used in original work.
- In order to have an estimate, we used the pretrained model provided by the authors at the original github link and then 
fine-tuned the model accordingly.
