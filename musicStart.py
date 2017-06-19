from readJson import ReadJson
from path import Path

import os
import pygame
import time
from mutagen.mp3 import MP3

class MusicStart:
    def single(self, number):
        readJson = ReadJson()
        path = Path()

        pwd = path.path()

        musicData = readJson.jsonSelector(number)

        audio = pwd + musicData

        audioLen = MP3(audio)
        pygame.mixer.init()
        pygame.mixer.music.load(audio)
        pygame.mixer.music.play(1)

        print("---"+ musicData +"---")

        time.sleep(audioLen.info.length)
        pygame.mixer.music.stop()

    def loop(self):
        readJson = ReadJson()
        path = Path()

        pwd = path.path()
        jsonNum = readJson.jsonNumber()

        for number in range(jsonNum):
            musicData = readJson.jsonSelector(number)

            audio = pwd + musicData

            audioLen = MP3(audio)
            pygame.mixer.init()
            pygame.mixer.music.load(audio)
            pygame.mixer.music.play(1)

            print("---"+ musicData +"---")

            time.sleep(audioLen.info.length)
            pygame.mixer.music.stop()

