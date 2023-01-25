from tkinter import*
from tkinter import ttk
from winsound import*
import time
from PIL import ImageTk, Image

splash_root = Tk()
splash_root.title("VIRUSVIRUSVIRUS")
splash_root.geometry("4000x4000")
splash_root.configure(bg="green")

img = ImageTk.PhotoImage(Image.open("Images\duck-white-png-image-purepng-transparent-png-82.png"))
panel = Label(splash_root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

def play_sound():
    check = False
    while check == False:
        PlaySound('Sounds\mixkit-cartoon-voice-laugh-343.mp3', SND_FILENAME)
        PlaySound('Sounds\wowowowowowowow-103214.mp3', SND_FILENAME)

splash_label = Label(splash_root, text="YOU HAVE A VIRUS", font=("Courier", 50))
splash_label.pack(pady=20)
button = ttk.Button(splash_root, text="CLICK HERE TO REMOVE", command = play_sound)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

splash_root.mainloop()