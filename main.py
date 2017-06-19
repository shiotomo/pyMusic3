from mode import Mode
from musicList import MusicList
from selectMusic import SelectMusic
from musicStartSingle import MusicStart
from musicStartLoop import MusicStart
from listUp import ListUp
from music import Music

def main():
    mode = Mode()
    musicList = MusicList()
    selectMusic = SelectMusic()
    musicStart = MusicStart()
    listUp = ListUp()
    music = Music()

    listUp.listUp()

    intmode = mode.selectMode()
    while intmode == "EOF":
        intmode = mode.selectMode()

    if intmode == "loop":
        print("\n")
        musicList.musicList()

    if intmode == "single":
        print("\n")
        musicList.musicList()
        number = selectMusic.selectMusic()
        musicStart.single(number)

if __name__ == '__main__':
    main()
