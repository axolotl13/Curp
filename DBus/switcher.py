"""
Copyright (c) 2023 Geovanni Santamaria. All Rights Reserved.
"""
from time import sleep

from brightness import Brightness


class Switcher(Brightness):
    def adjust_brightness(self, screen, brightness, value_file):
        if brightness == value_file:
            return

        step = 5 if brightness <= value_file else -5

        while brightness != value_file:
            screen.StepUp() if step > 0 else screen.StepDown()
            brightness += step
            sleep(0.1)

    def on(self):
        try:
            brightness = self.brightness()
            value_file = int(self.timeformat())
            print(f"value_file{value_file}, brightness{brightness}")
            screen = self.screen
            # value_file = round(value_file / 5) * 5
            self.adjust_brightness(screen, brightness, value_file)
        except ValueError:
            print("No values found")


Switcher().on()
