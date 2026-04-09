import pygame
import tkinter as tk

pygame.mixer.init()

songs = {
    "happy": "happy.mp3",
    "sad": "sad.mp3",
    "angry": "angry.mp3",
    "neutral": "neutral.mp3"
}

def play_music(mood):
    if mood in songs:
        pygame.mixer.music.load(songs[mood])
        pygame.mixer.music.play()
        status_label.config(text=f"Playing {mood} song", fg="green", bg="#000000")
    else:
        status_label.config(text="Invalid mood!", fg="red", bg="#000000")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="Music Stopped", fg="red", bg="#000000", font=("Wide Latin", 45))

root = tk.Tk()
root.title("Mood Music Player")
root.geometry("500x500")


root.configure(bg="#000000")   


title = tk.Label(root, text="Mood Music Player",
                 font=("Algerian", 55),
                 fg="yellow", bg="#000000")
title.pack(pady=10)


tk.Button(root, text="Happy", font=("Times New Roman", 30),
          width=50, bg="green", fg="white",
          command=lambda: play_music("happy")).pack(pady=20)

tk.Button(root, text="Sad", font=("Times New Roman", 30),
          width=50, bg="blue", fg="white",
          command=lambda: play_music("sad")).pack(pady=20)

tk.Button(root, text="Angry", font=("Times New Roman", 30),
          width=50, bg="orange", fg="black",
          command=lambda: play_music("angry")).pack(pady=20)

tk.Button(root, text="Neutral", font=("Times New Roman", 30),
          width=50, bg="gray", fg="white",
          command=lambda: play_music("neutral")).pack(pady=20)


tk.Button(root, text="Stop Music", font=("Arial", 30),
          width=20, bg="red", fg="white",
          command=stop_music).pack(pady=15)

# Status label
status_label = tk.Label(root, text="",
                        fg="white", bg="#000000",
                        font=("Arial", 12))
status_label.pack()

root.mainloop()