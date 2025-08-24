import RPi.GPIO as GPIO
import os
import time

# pi shutdown script XDXDXDXDXDXDXDXDXDXD
# short press <5s = clean shutdown
# long press >=5s = reboot

BUTTON_PIN = 3  # GPIO3 (physical pin 5) 
LONG_PRESS_TIME = 5  # long press = reboot
COUNTDOWN = 3  # seconds countdown before action

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Power button handler running. Short press = shutdown, long press = reboot.")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # button pressed
            press_time = time.time()
            while GPIO.input(BUTTON_PIN) == GPIO.LOW:
                time.sleep(0.1)
            held_time = time.time() - press_time

            if held_time >= LONG_PRESS_TIME:
                print(f"Button held for {held_time:.1f}s → Rebooting in {COUNTDOWN}s...")
                for i in range(COUNTDOWN, 0, -1):
                    print(f"{i}...")
                    time.sleep(1)
                os.system("sudo reboot")
            else:
                print(f"Button held for {held_time:.1f}s → Shutting down in {COUNTDOWN}s...")
                for i in range(COUNTDOWN, 0, -1):
                    print(f"{i}...")
                    time.sleep(1)
                os.system("sudo shutdown now")

        time.sleep(0.1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
