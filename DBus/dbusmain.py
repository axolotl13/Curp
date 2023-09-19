from datetime import datetime
from pathlib import PurePath

from pydbus import SessionBus


class main:
    def __init__(self) -> None:
        # Usa la librería pydbus para establecer algún valor para cambiar brillo.
        bus = SessionBus()
        self.screen = bus.get("org.gnome.SettingsDaemon.Power")[".Screen"]
        # Ruta para almacenar el valor del brillo actual.
        self.logfile = PurePath("/home", "joker", "Escritorio", "logs")
        # Ruta del archivo del brillo para monitoriar
        self.path = PurePath(
            "/sys", "class", "backlight", "intel_backlight", "brightness"
        )
        # Obtiene la hora ctual del sistema.
        self.time = datetime.now()

    def getTimeValue(self):
        # Establece la hora actual en numeros enteros.
        now = self.time
        now = int(now.strftime("%H%M"))
        # Guarda el valor en el archivo especifico segun la hora.
        # Retorna el valor si la hora cumple con el rango establecido.
        return {
            now in range(700, 730): "700",
            now in range(730, 800): "730",
            now in range(800, 830): "800",
            now in range(830, 900): "830",
            now in range(900, 930): "900",
            now in range(930, 1000): "930",
            now in range(1000, 1030): "1000",
            now in range(1030, 1100): "1030",
            now in range(1100, 1130): "1100",
            now in range(1130, 1200): "1130",
            now in range(1200, 1230): "1200",
            now in range(1230, 1300): "1230",
            now in range(1300, 1330): "1300",
            now in range(1330, 1400): "1330",
            now in range(1400, 1430): "1400",
            now in range(1430, 1500): "1430",
            now in range(1500, 1530): "1500",
            now in range(1530, 1600): "1530",
            now in range(1600, 1630): "1600",
            now in range(1630, 1700): "1630",
            now in range(1700, 1730): "1700",
            now in range(1730, 1800): "1730",
            now in range(1800, 1830): "1800",
            now in range(1830, 1900): "1830",
            now in range(1900, 1930): "1900",
            now in range(1930, 2000): "1930",
            now in range(2000, 2030): "2000",
            now in range(2030, 2100): "2030",
            now in range(2100, 2130): "2100",
            now in range(2130, 2200): "2130",
            now in range(2200, 2230): "2200",
            now in range(2230, 2300): "2230",
            now in range(2300, 2330): "2300",
            now in range(2330, 2400): "2330",
        }.get(True, "0")

    # Obtiene el valor del brillo actualmente y lo retorna en un string y lo redondea.
    def getBrightnessValue(self):
        screen = self.screen
        return str(round(screen.Brightness / 5) * 5)
        #     if screen.StepUp()[0] >= 61:
