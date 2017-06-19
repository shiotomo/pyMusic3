import os
import json

from path import Path

class ListUp:
    def listUp(self):
        path = Path()

        fileList = {}

        for i, file in enumerate(os.listdir(path.path())):
            fileList[i] = file

        listFile = open('list.json', 'w')
        json.dump(fileList, listFile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        listFile.close()
