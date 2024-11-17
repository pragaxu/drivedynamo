import tkinter as tk
from sensors import get_sensor_data
from eye_blink import detect_blink
from cabin_adjustment import determine_emotion, adjust_cabin

root = tk.Tk()
root.title("Smart Car Cabin Prototype")

emotion_label = tk.Label(root, text="Emotion: N/A", font=("Helvetica", 16))
emotion_label.pack()

def update_display():
    heart_rate, skin_temp = get_sensor_data()
    blink_rate = detect_blink()
    emotion = determine_emotion(heart_rate, skin_temp, blink_rate)
    adjust_cabin(emotion)
    emotion_label.config(text=f"Emotion: {emotion.capitalize()}")
    root.after(1000, update_display)  # Update every second

update_display()
root.mainloop()
