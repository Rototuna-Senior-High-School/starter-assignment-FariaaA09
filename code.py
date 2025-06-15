import board
import pwmio
import analogio
import time

knob = analogio.AnalogIn(board.A0)

led = pwmio.PWMOut(board.GP3, frequency=1000, duty_cycle=0)
led2 = pwmio.PWMOut(board.GP0, frequency=1000, duty_cycle=0)

while True:
    knob_value = knob.value  # 0–65535
    print("Knob:", knob_value)

    if knob_value < 32768:
        led.duty_cycle = knob_value * 2
        led2.duty_cycle = 0
    else:
        led.duty_cycle = 65535
        led2_value = (knob_value - 32768) * 2
        if led2_value > 65535:
            led2_value = 65535
        led2.duty_cycle = led2_value

    time.sleep(0.01)
