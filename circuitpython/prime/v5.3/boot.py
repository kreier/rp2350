# toggle the write switch to the local file system 2026/10/08

import time
import board
import digitalio
import storage

BUTTON_PIN = board.GP10
COUNTDOWN  = 5

# T-Display rp2040     board.BUTTON_L    False if pressed
# T-Display ESP32-S2   board.IO0
# Waveshare rp2350     board.GP0         False if connected to GND

# GP0 is active-low: button connected to GND = pressed
button = digitalio.DigitalInOut(BUTTON_PIN)
button.switch_to_input(pull=digitalio.Pull.UP)

# On-board LED
led = digitalio.DigitalInOut(board.LED)
led.switch_to_output(value=True)

print(f"Press the button within {COUNTDOWN} seconds to enable filesystem writes")

start = time.monotonic()
last_second = COUNTDOWN

while time.monotonic() - start < COUNTDOWN:
    # Button pressed?
    if not button.value:
        print("Write access activated")
        storage.disable_usb_drive()
        led.value = False
        break

    # Countdown display
    remaining = COUNTDOWN - int(time.monotonic() - start)

    if remaining != last_second:
        last_second = remaining
        print(remaining)

    time.sleep(0.05)

else:
    # Button was not pressed
    print("Not activated")
    led.value = True

time.sleep(0.5)
