# from tkinter import *
# from tkinter import Tk
# import time
# import datetime
# from PIL import ImageTk
# from tkinter import ttk, messagebox
# from pygame import mixer
#
#
#
# hourList = ['00', '01', '02', '03', '04', '05', '06', '07',
#             '08', '09', '10', '11', '12', '13', '14', '15',
#             '16', '17', '18', '19', '20', '21', '22', '23', '24']
# minuteList = ['00', '01', '02', '03', '04', '05', '06', '07',
#               '08', '09', '10', '11', '12', '13', '14', '15',
#               '16', '17', '18', '19', '20', '21', '22', '23',
#               '24', '25', '26', '27', '28', '29', '30', '31',
#               '32', '33', '34', '35', '36', '37', '38', '39',
#               '40', '41', '42', '43', '44', '45', '46', '47',
#               '48', '49', '50', '51', '52', '53', '54', '55',
#               '56', '57', '58', '59']
# ringtoneList = [ 'Night-Changes-Ringtone-Dwonload', 'twirling_intime']
# ringtonePath = { 'Night-Changes-Ringtone-Dwonload': 'ringtone/Night-Changes-Ringtone-Dwonload.mp3',
#                 'twirling_intime': 'ringtone/twirling_intime.mp3'}
#
#
# class Alarm_Clock:
#
#     def __init__(self, root):
#         super().__init__()
#         self.window = root
#         self.window.geometry('800x520+0+0')
#         self.window.title("Alarm Clock")
#         # background image
#         self.backgroundimage = ImageTk.PhotoImage(file='alarm_image.jpg')
#         self.background = Label(self.window, image=self.backgroundimage)
#         self.background.place(x=0, y=0, relwidth=1, relheight=1)
#
#         # current time
#         self.dispaly = Label(self.window)
#         self.dispaly.place(x=200, y=150)
#
#         self.currenttime()
#
#         # set alarm button
#         set_button = Button(self.window, text="Set Alarm", font=('Helvetica', 15), bg="purple", fg="white",command=self.anotherwindow)
#         set_button.pack(padx=200, pady=220)
#
#     def currenttime(self):
#         showtime = time.strftime("%H:%M:%S %p ,%A ,%x")
#         self.dispaly.config(text=showtime, font="CourierNew 20 bold")
#         self.dispaly.after(100, self.currenttime)
#
#     def status(self):
#         self.var = StringVar()
#
#     def anotherwindow(self):
#         self.anotherwindow = Tk()
#         self.anotherwindow.geometry("780x420")
#         self.anotherwindow.title("clock")
#
#         hour = Label(self.anotherwindow, text="Hours",
#                      font="lucida 15 bold")
#         hour.place(x=170, y=50)
#
#         min = Label(self.anotherwindow, text="Minutes",
#                     font="lucida 15 bold")
#         min.pack(pady=50)
#
#         self.hour = StringVar()
#         self.hour_Combobox = ttk.Combobox(self.anotherwindow,
#                                            width=10, height=10,
#                                           textvariable=self.hour,font="lucida 10")
#         self.hour_Combobox["values"] = hourList
#         self.hour_Combobox.current(0)
#         self.hour_Combobox.place(x=240, y=55)
#
#         self.min = StringVar()
#         self.min_Combobox = ttk.Combobox(self.anotherwindow,
#                                           width=10, height=10, textvariable=self.min,font="lucida 10")
#         self.min_Combobox["values"] = minuteList
#         self.min_Combobox.current(0)
#         self.min_Combobox.place(x=440, y=55)
#
#         # ringtone  lable
#         ringtone = Label(self.anotherwindow, text="Ringtone",
#                          font="lucida 15 bold")
#         ringtone.place(x=170, y=100)
#         self.ringtone = StringVar()
#         self.ringtone_Combobox = ttk.Combobox(self.anotherwindow, width=15,
#                                               height=15, textvariable=self.ringtone,font="lucida 10")
#         self.ringtone_Combobox["values"] = ringtoneList
#         self.ringtone_Combobox.current(0)
#         self.ringtone_Combobox.place(x=270, y=105)
#
#         messagebox = Label(self.anotherwindow, text="Message",
#                            font="lucida 15 bold")
#         messagebox.place(x=170, y=150)
#         self.messagebox = StringVar()
#         self.messagebox_entry = Entry(self.anotherwindow, textvariable=self.messagebox,font="lucida 10")
#         self.messagebox_entry.insert(0, 'Good Morning')
#         self.messagebox_entry.place(x=270, y=155)
#
#         button = Button(self.anotherwindow, text="Start", height=1, width=10,bg="blue",fg="white",font="lucida 15", command=set)
#         button.place(x=170, y=205)
#
#         button = Button(self.anotherwindow, text="Cancle", height=1, width=10,font="lucida 15",command=self.anotherwindow.destroy)
#         button.place(x=280, y=205)
#
#         self.anotherwindow.mainloop()
#
#     mixer.init()
#
#     def set(self):
#
#        if alarmtime == currenttime:
#             mixer.music.load("Night-Changes-Ringtone-Download.mp3")
#             mixer.music.play()
#        else:
#             msg = messagebox.showerror('invalid time')
#
# root = Tk()
# object = Alarm_Clock(root)
#
# root.mainloop()


from tkinter import *
from tkinter import filedialog
from os import path
from PIL import ImageTk, Image
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from tkinter import messagebox
import shutil


# functions
def selectPath():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def downloadFile():
    # user path
    get_link = link_entry.get()
    # selected path
    user_path = path_label.cget("text")
    root.title('Downloading....')
    # download video
    videoFile = YouTube(get_link).streams.first().download()
    # move to selected directory
    root.title('Download Complete')
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + user_path)


root = Tk()
root.title("Youtube Video Downloader")
canvas = Canvas(root, width=500, height=500)
canvas.pack()
# image
img = PhotoImage(file='download.png')
img = img.subsample(4, 4)
canvas.create_image(250, 80, image=img)
# link
link_entry = Entry(root, width=50)
link_label = Label(root, text="Enter download link:", font=('Arial', 15))
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 200, window=link_entry)
# path for saving file
path_label = Label(root, text="Select Path For Download", font=('Arial', 15))
select_button = Button(root, text="Select", command=selectPath)
canvas.create_window(250, 250, window=path_label)
canvas.create_window(250, 300, window=select_button)
# Download button
download_button = Button(root, text="Download video", command=downloadFile)
canvas.create_window(250, 350, window=download_button)
root.mainloop()
