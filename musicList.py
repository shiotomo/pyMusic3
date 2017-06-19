import os
import glob
from path import Path

class MusicList:
    def musicList(self):
        path = Path()

        files = glob.glob(path.path() + '*.mp3')

        print("--- Music List ---")
        for index, file in enumerate(files):
            print('{0} : {1}' . format(index, file))
        print("------------------")
        return files
