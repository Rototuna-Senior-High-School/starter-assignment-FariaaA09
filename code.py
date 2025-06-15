# Import Pi Pico board so we can talk to the pins
import board

# Import PWM (Pulse Width Modulation) to dim LEDs
import pwmio

# Import Analog input to read the potentiometer (knob)
import analogio

# Import time to add small delays (smooth transitions)
import time

# The potentiometer is connected to A0
knob = analogio.AnalogIn(board.A0)

# Set up two LEDs with PWM (so we can fade them)
ledred = pwmio.PWMOut(board.GP3, frequency=1000, duty_cycle=0)
ledblue = pwmio.PWMOut(board.GP0, frequency=1000, duty_cycle=0)

# Loop forever
while True:
# Read the potentiometer value (0 to 65535)
    knob_value = knob.value
    print("Knob:", knob_value)

# If knob is in the lower half (0–32767), fade in red LED
    if knob_value < 32768:
        ledred.duty_cycle = knob_value * 2
        ledblue.duty_cycle = 0

# If knob is in the upper half (32768–65535), keep red on and fade in blue
    else:
        ledred.duty_cycle = 65535
        ledblue_value = (knob_value - 32768) * 2

        if ledblue_value > 65535:
            ledblue_value = 65535

        ledblue.duty_cycle = ledblue_value

# Wait a tiny bit to smooth it out
    time.sleep(0.01)
