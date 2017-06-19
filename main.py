from mode import Mode
from musicList import MusicList
from selectMusic import SelectMusic
from musicStart import *
from listUp import ListUp

def main():
    mode = Mode()
    musicList = MusicList()
    selectMusic = SelectMusic()
    musicStart = MusicStart()
    listUp = ListUp()

    listUp.listUp()

    modeFlag = mode.selectMode()
    while modeFlag == "EOF":
        modeFlag = mode.selectMode()

    if modeFlag == "loop":
        print("\n")
        musicList.musicList()
        print("\n")
        musicStart.loop()

    if modeFlag == "single":
        print("\n")
        musicList.musicList()
        number = selectMusic.selectMusic()
        print("\n")
        musicStart.single(number)

if __name__ == '__main__':
    main()
