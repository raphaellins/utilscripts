from pytube import YouTube

import os
import shutil
import math
import datetime

video = YouTube('youtube video')

print('Summary:')
print(f'Title: {video.title}')
print(f'Duration: {video.length / 60:.2f} minutes')
print(f'Rating: {video.rating:.2f}')
print(f'# of views: {video.views}')

video_streams = video.streams.all()

for videos in video_streams:
    print(videos)

# video.streams.filter(file_extension="mp4").all()

video.streams.get_by_itag(22).download()
