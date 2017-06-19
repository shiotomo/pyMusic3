import os

class Path:
    def path(self):
        musicpath = os.path.abspath(os.path.dirname(__file__))
        musicpath = musicpath + "/Music/"
        return musicpath
