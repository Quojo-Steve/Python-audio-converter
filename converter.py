import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

name = input("Enter your prefered file name ")
audio.write_audiofile(name+".mp3")
print("completed")
