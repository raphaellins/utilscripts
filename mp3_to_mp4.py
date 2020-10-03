import os
from os import walk

mypath = 'your path'

f = []
for (dirpath, dirnames, filenames) in walk(mypath):

    for file in filenames:
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.mp3':
            ffmpeg_cmd = "ffmpeg -loop 1 -r 1 -i pic.jpg -i '" + mypath + "/" + file + \
                "' -c:a copy -shortest -vcodec mpeg4 '" + mypath + "/" + filename + ".mp4'"
            os.system(ffmpeg_cmd)
