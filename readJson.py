import os
import json

class ReadJson:
    def jsonSelector(self, number):
        number = str(number)
        try:
            maybeJson = open('list.json', 'r')
        except OSError as i:
            print(i.errno + i.strerror)

        try:
            jsonData = json.load(maybeJson)
        except json.JSONDecodeError as e:
            print(e.pos + e.msg)

        '''
        print(number)
        print(jsonData)
        print(jsonData[number])
        '''

        maybeJson.close()

        return jsonData[number]

    def jsonNumber(self):
        try:
            maybeJson = open('list.json', 'r')
        except OSError as i:
            print(i.errno + i.strerror)

        try:
            jsonData = json.load(maybeJson)
        except json.JSONDecodeError as e:
            print(e.pos + e.msg)

        maybeJson.close()

        jsonNum = len(jsonData)

        return jsonNum
