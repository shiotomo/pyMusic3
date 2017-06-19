from music import Music

import os
import json

class MusicStart:
    def music(Music, number):
        try:
            maybeJson = open('list.json', 'r')
        except OSError as i:
            print(i.errno + i.strerror)

        try:
            jsonData = json.load(maybeJson)
        except json.JSONDecodeError as e:
            print(e.pos + e.msg)

        print(number)
        print(jsonData)
        print(jsonData[number])

        maybeJson.close()

