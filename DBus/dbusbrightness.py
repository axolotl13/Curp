from time import sleep

from dbusmain import main


class brightness(main):
    def getRoulette(self):
        try:
            # Escribe en el archivo el valor del brillo dependiendo la hora.
            getBrightness = int(self.getBrightnessValue())
            time_logfile = open(self.logfile.joinpath(self.getTimeValue()), "r")
            getTime = int(time_logfile.read())
            screen = self.screen
            # [screen.StepUp() for _ in range(brillo, getTime, 5)]
            if getBrightness == getTime:
                pass
            elif getBrightness <= getTime:
                for _ in range(getBrightness, getTime, 5):
                    screen.StepUp()
                    sleep(0.1)
            elif getBrightness >= getTime:
                for _ in range(getBrightness, getTime, -5):
                    screen.StepDown()
                    sleep(0.1)
            else:
                pass
        except FileNotFoundError:
            print("File Not Found")


run = brightness()
run.getRoulette()
