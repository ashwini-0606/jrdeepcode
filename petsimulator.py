import tkinter as tk
import random

#Functions
def feed_pet():
    global mood_timer_id
    if mood_timer_id:
        root.after_cancel(mood_timer_id)
        mood_timer_id = None

    if new_mood == "Gengar is hungry!":
        label.config(text="Yum! Your pet is super full!")
        root.after(2000, happy_pet)

        global current_img
        current_img = tk.PhotoImage(file="happy.png")
        img_label.config(image=current_img)  
    elif new_mood == "Happy": 
        label.config(text="Gengar doesn't need anything!")
        root.after(2000, happy_pet) 
    else:
        label.config(text="Wrong choice!")

def pet_pet():
    global mood_timer_id
    if mood_timer_id:
        root.after_cancel(mood_timer_id)
        mood_timer_id = None
        
    if new_mood == "Gengar wants to play with you!":
        label.config(text="Your pet is happy to have played with you!")
        root.after(2000, happy_pet)

        global current_img
        current_img = tk.PhotoImage(file="happy.png")
        img_label.config(image=current_img)
    elif new_mood == "Happy": 
        label.config(text="Gengar doesn't need anything!")
        root.after(2000, happy_pet) 
    else:
        label.config(text="Wrong choice!")

def clean_pet():
    global mood_timer_id
    if mood_timer_id:
        root.after_cancel(mood_timer_id)
        mood_timer_id = None
        
    if new_mood == "Gengar is dirty...":
        label.config(text="Perfect! Your pet is now clean!")
        root.after(2000, happy_pet) 

        global current_img
        current_img = tk.PhotoImage(file="happy.png")
        img_label.config(image=current_img)
    elif new_mood == "Happy": 
        label.config(text="Gengar doesn't need anything!")
        root.after(2000, happy_pet) 
    else:
        label.config(text="Wrong choice!")

def happy_pet():
    global mood_timer_id
    label.config(text="Gengar is happy!")
    global new_mood
    new_mood = "Happy"

    global current_img
    current_img = tk.PhotoImage(file="happy.png")
    img_label.config(image=current_img)
    mood_timer_id = root.after(3000, update_mood)


def update_mood():
    moods = [
        ("Gengar is hungry!", "hungry.png"),
        ("Gengar wants to play with you!", "sad.png"),
        ("Gengar is dirty...", "dirty.png")
    ]
    global new_mood
    new_mood, new_img_path = random.choice(moods)
    label.config(text=new_mood)

    global current_img
    current_img = tk.PhotoImage(file=new_img_path)
    img_label.config(image=current_img)

#Creating the Window
root = tk.Tk()
root.state("zoomed")
root.title("Python Pet Simuator")

#Background
bg = tk.PhotoImage(file="background.png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Setting Main Label
label = tk.Label(root, font=("Comic Sans MS", 24, "bold italic"), text="Gengar is happy!")
label.pack()

#Setting Image of the Pet
img = tk.PhotoImage(file="happy.png")
img_label = tk.Label(root, image=img)
img_label.place(x=420, y=200)  # absolute position

#Setting the Buttons
button_frame = tk.Frame(root, bg="#ffffff")  # optional bg to match layout
button_frame.pack(pady=20)

btn = tk.Button(button_frame, font=("Arial", 16), text="Feed", command=feed_pet)
btn.pack(side="left", padx=10)

btn2 = tk.Button(button_frame, font=("Arial", 16), text="Pet", command=pet_pet)
btn2.pack(side="left", padx=10)

btn2 = tk.Button(button_frame, font=("Arial", 16), text="Clean", command=clean_pet)
btn2.pack(side="left", padx=10)

# Start the repeating loop
happy_pet()
# 3. Run the app
root.mainloop()