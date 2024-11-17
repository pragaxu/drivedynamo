import board
import busio
import adafruit_mlx90614
import time
from gpiozero import MCP3008  # For analog heart rate sensor

# Initialize I2C bus for temperature sensor
i2c = busio.I2C(board.SCL, board.SDA)
temp_sensor = adafruit_mlx90614.MLX90614(i2c)

# Initialize heart rate sensor
heart_rate_sensor = MCP3008(channel=0)

def get_sensor_data():
    heart_rate = heart_rate_sensor.value * 100  # Convert analog to heart rate
    skin_temp = temp_sensor.object_temperature
    return heart_rate, skin_temp
