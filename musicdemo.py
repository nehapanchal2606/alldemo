# import time
# from pygame import mixer
#
# def playmusic(name):
#     mixer.init()
#     mixer.music.load(name)
#     # mixer.music.set_volume(0.7)
#     mixer.music.play()
#     while mixer.music.get_busy():
#         time.process_time()
#
# playmusic('musicfile.mp3')
#
# x = int(input("Enter Num: "))
# while(True):
#     if(x==1):
#         mixer.music.stop()
#         break
#     else:
#         continue


import vlc
a = vlc.Med('musicfile.mp3')