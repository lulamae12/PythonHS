#!/usr/bin/env python
import os, sys, time
import argparse
from urllib.request import urlopen

import pytube  # pip install pytube


CS294_playlist_url = "https://www.youtube.com/playlist?list=PLKJ7g305OHDEUNF_BzAUdcxt4d_ey8m6z"


def get_playlist_links(playlist_url):
    page_elements = urlopen(playlist_url).readlines()
    video_elements = [el for el in page_elements if 'pl-video-title-link' in el]  # Filter out unnecessary lines
    video_urls = [v.split('href="',1)[1].split('" ',1)[0] for v in video_elements]  # Grab the video urls from the elements
    return ['http://www.youtube.com' + v for v in video_urls]


start_time = time.time()

def print_dot(bytes_received, file_size, start):
    global start_time
    if time.time() - start_time > 1.0:
        sys.stdout.write('.')
        sys.stdout.flush()
        start_time = time.time()


parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-p PLAYLISTURL] [-d DESTINATION]')
parser.add_argument('-p', '--playlisturl', help='url of the playlist to be downloaded', default=CS294_playlist_url, metavar='')
parser.add_argument('-d', '--destination', help='path of directory to save videos to', default=os.path.curdir, metavar='')
args = parser.parse_args()


if os.path.exists(args.destination):
    directory_contents = [f.split('.mp3',1)[0] for f in os.listdir(args.destination) if f.endswith('.mp3')]
else:
    print('Destination directory does not exist')
    sys.exit(1)

video_urls = get_playlist_links(args.playlisturl)
confirmation = raw_input('You are about to download {} videos to {}\nWould you like to continue? [Y/n] '.format(
    len(video_urls), os.path.abspath(args.destination)))

if confirmation.lower() in ['y', '']:
    for u in video_urls:
        yt = pytube.YouTube(u)
        vid = yt.streams.filter(file_extension='mp4').order_by('res').last() # grab the highest resolution mp4 file

        if vid.default_filename in directory_contents:
            print('Skipping {}'.format(vid.default_filename))
            continue
        else:
            print('Downloading {}'.format(vid.default_filename))
            vid.download(args.destination)
            print('Done')
