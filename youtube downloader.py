from pytube import *


def p():
    o = input('> ')

    try:
        url = YouTube(str(o))
        video = url.streams.first()
        video.download()
        print('video successfully downloaded')
    except Exception as e:
        print(e)
        p()


p()