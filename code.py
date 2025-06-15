import time
import board
import analogio
import digitalio

knob = analogio.AnalogIn(board.A0)

transistor_pin = digitalio.DigitalInOut(board.GP15)
transistor_pin.direction = digitalio.Direction.OUTPUT

while True:
    analog_value = knob.value

    print('raw = ' + str(knob.value))

    delay_time = analog_value / 20000

    transistor_pin.value = True
    print(f"LEDs ON for {delay_time:.2f} seceonds")
    time.sleep(delay_time)

    transistor_pin.value = False
    print(f"LEDs OFFfor {delay_time:.2f} seceonds")
    time.sleep(delay_time)
