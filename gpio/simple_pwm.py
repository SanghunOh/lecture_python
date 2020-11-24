import Jetson.GPIO as GPIO
import time

# output_pins = {
#     'JETSON_XAVIER': 18,
#     'JETSON_NANO': 33,
#     'JETSON_NX': 33,
#     'CLARA_AGX_XAVIER': 18,
# }
# output_pin = output_pins.get(GPIO.model, None)
# if output_pin is None:
#     raise Exception('PWM not supported on this board')

output_pin = 33
def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    pwm = GPIO.PWM(output_pin, 50)
    val = 25
    incr = 5
    pwm.start(val)

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.25)
            if val >= 100:
                incr = -incr
            if val <= 0:
                incr = -incr
            val += incr
            pwm.ChangeDutyCycle(val)
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()