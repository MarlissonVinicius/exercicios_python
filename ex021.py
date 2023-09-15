#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("ex021.mp3")
play(song)