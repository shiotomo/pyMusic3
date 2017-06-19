from readJson import *

import os
import json

class MusicStart:
    def single(self, number):
        readJson = ReadJson()
        musicData = readJson.JsonSelector(number)
        print(musicData)

    def loop(self, number):
        pass
