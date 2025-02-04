import tkinter as tk
from tkinter import PhotoImage
import json
import random
import os

# Constants
auto_duration = 5 # seconds

# Load flashcard data
with open("patterns.json", "r") as file:
    flashcards = json.load(file)

# Initialize global variables
current_flashcard = None
previous_flashcard = None
auto_mode = False
countdown = None

def load_random_flashcard():
    global current_flashcard, previous_flashcard, countdown
    
    if countdown:
        root.after_cancel(countdown)
    
    new_flashcard = random.choice(flashcards)
    while new_flashcard == previous_flashcard:
        new_flashcard = random.choice(flashcards)
    
    current_flashcard = new_flashcard
    previous_flashcard = current_flashcard
    img_path = os.path.join("patterns", current_flashcard["image"])
    
    if os.path.exists(img_path):
        image = PhotoImage(file=img_path)
        canvas.itemconfig(image_container, image=image)
        canvas.image = image
    else:
        canvas.itemconfig(image_container, image=None)
    
    canvas.config(highlightbackground="grey", highlightthickness=3)
    reveal_button.config(text="Reveal", command=reveal_info)
    info_label_name.config(text=" ")
    info_label_signal.config(text=" ")
    info_label_type.config(text=" ")
    
    if auto_mode:
        start_timer(auto_duration, reveal_info)

def reveal_info():
    global countdown
    info_label_name.config(text=f"Name: {current_flashcard['name']}")
    info_label_signal.config(text=f"Signal: {current_flashcard['signal']}")
    info_label_type.config(text=f"Type: {current_flashcard['type']}")
    
    if current_flashcard['signal'].lower() == "bullish":
        canvas.config(highlightbackground="green")
    elif current_flashcard['signal'].lower() == "bearish":
        canvas.config(highlightbackground="red")
    else:
        canvas.config(highlightbackground="grey")
    
    reveal_button.config(text="Next", command=load_random_flashcard)
    
    if auto_mode:
        start_timer(auto_duration, load_random_flashcard)

def toggle_auto_mode():
    global auto_mode
    auto_mode = not auto_mode
    if auto_mode:
        auto_button.config(bg="green", text="Auto On")
        timer_label.pack()
        start_timer(auto_duration, reveal_info)
    else:
        auto_button.config(bg="red", text="Auto Off")
        timer_label.pack_forget()

def start_timer(seconds, callback):
    global countdown
    if seconds > 0:
        timer_label.config(text=f"{seconds}s")
        countdown = root.after(1000, start_timer, seconds - 1, callback)
    else:
        callback()

# Create UI
root = tk.Tk()
root.title("Candlestick Trainer")
root.configure(bg="#060912")

frame = tk.Frame(root, bg="#060912")
frame.pack(pady=10, padx=10)

canvas = tk.Canvas(frame, width=300, height=300, highlightthickness=3, bg="#060912")
canvas.pack()
image_placeholder = PhotoImage()
image_container = canvas.create_image(150, 150, image=image_placeholder)

info_frame = tk.Frame(frame, height=60, bg="#060912")
info_frame.pack()
info_label_name = tk.Label(info_frame, text=" ", font=("Arial", 12), bg="#060912", fg="white")
info_label_name.pack()
info_label_signal = tk.Label(info_frame, text=" ", font=("Arial", 12), bg="#060912", fg="white")
info_label_signal.pack()
info_label_type = tk.Label(info_frame, text=" ", font=("Arial", 12), bg="#060912", fg="white")
info_label_type.pack()

reveal_button = tk.Button(frame, text="Reveal", command=load_random_flashcard, font=("Arial", 14))
reveal_button.pack(pady=5)

auto_button = tk.Button(frame, text="Auto Off", command=toggle_auto_mode, font=("Arial", 14), bg="red")
auto_button.pack(pady=5)

timer_label = tk.Label(frame, text="", font=("Arial", 12), bg="#060912", fg="white")

# Start with the first flashcard
load_random_flashcard()

root.mainloop()
