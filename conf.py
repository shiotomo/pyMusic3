import os

class Conf:
    def existence(self):
        if os.path.isdir("Music"):
            pass
        else:
            os.mkdir(Music)
