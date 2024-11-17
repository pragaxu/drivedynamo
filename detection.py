from gpiozero import LED, Buzzer
import time

# Initialize components
led = LED(17)       # RGB LED (example GPIO)
fan = LED(27)       # Fan or heater control
buzzer = Buzzer(22) # Buzzer for alert

def determine_emotion(heart_rate, skin_temp, blink_rate):
    if heart_rate > 100 and blink_rate < 10:
        return "stressed"
    elif blink_rate > 15:
        return "fatigued"
    else:
        return "calm"

def adjust_cabin(emotion):
    if emotion == "stressed":
        led.on()      # Example: turn blue light on
        fan.off()
    elif emotion == "fatigued":
        led.on()      # Example: white light for alertness
        fan.on()      # Turn on fan for cooling effect
        buzzer.on()
        time.sleep(0.5)
        buzzer.off()
    elif emotion == "calm":
        led.on()      # Example: green light for calm
        fan.off()
