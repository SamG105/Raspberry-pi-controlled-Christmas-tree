from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import serial
from flask import Flask, render_template, request
import threading

# ... (your existing imports)

app = Flask(__name__)

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# Compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

# Initialize the LCD class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)
water_level = 0
water_level_history = 0

# Set up the serial connection to Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

christmas_date = datetime(year=datetime.now().year + 1, month=1, day=1)
# Wipe LCD screen before we start
lcd.clear()

# Define default RGB values
default_red = 128
default_green = 128
default_blue = 128

# Thread flag to stop the loop when the Flask app is terminated
stop_thread = False

def lcd_and_led_loop():
    global water_level, water_level_history, default_red, default_green, default_blue
    while not stop_thread:
        if ser.in_waiting > 0:
            water_level = ser.read().decode('ascii').rstrip()

        if water_level != water_level_history:
            water_level_history = water_level
            print(water_level)

        lcd_line_2 = str(water_level)

        time_remaining = christmas_date - datetime.now()

        lcd_line_1 = str(time_remaining)#time_remaining.strftime('%b %d  %H:%M:%S\n')
        print("lcd line 1:")
        print(str(time_remaining))

        lcd.message = lcd_line_1 + lcd_line_2

        sleep(1)

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    time_remaining = christmas_date - datetime.now()
    global default_red, default_green, default_blue

    if request.method == 'POST':
        # Retrieve the current values from the form submission
        red = int(request.form.get('red', default_red))
        green = int(request.form.get('green', default_green))
        blue = int(request.form.get('blue', default_blue))

        # Update RGB LEDs
        ser.write(f"{red},{green},{blue}".encode('ascii'))

        # Set the default values for the next rendering
        default_red, default_green, default_blue = red, green, blue
    return render_template('index.html', time_remaining=str(time_remaining), water_level=str(water_level), default_red=default_red, default_green=default_green, default_blue=default_blue)

# Start the infinite loop in a separate thread
loop_thread = threading.Thread(target=lcd_and_led_loop)
loop_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

    # Set the flag to stop the thread when the Flask app is terminated
    stop_thread = True
    loop_thread.join()  # Wait for the thread to finish before exiting

