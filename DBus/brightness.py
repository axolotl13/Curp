"""
Copyright (c) 2023 Geovanni Santamaria. All Rights Reserved.
"""
from datetime import datetime
from pathlib import Path

from pydbus import SessionBus


class Brightness:
    """
    Attributes:
        screen: Usa la librería pydbus para cambiar el valor del brillo.
        logfile: Ruta que usa para almacenar los valores del brillo.
        brifile: Ruta en el que se encuntra el archivo del brillo.
        currentime: Obtiene la hora actual.
    """

    logs = Path("/tmp/logs")

    def __init__(self) -> None:
        try:
            bus = SessionBus()
            self.screen = bus.get("org.gnome.SettingsDaemon.Power")[".Screen"]
            self.logfile = self.logs.mkdir() if not self.logs.exists() else self.logs
            self.brifile = Path("/sys/class/backlight/amdgpu_bl1/brightness")
            self.currentime = datetime.now()
        except FileNotFoundError as ex:
            raise ex

    def timeformat(self) -> str:
        """
        Guarda el valor en el archivo especifico segun la hora.
        Retorna el valor si la hora cumple con el rango establecido.
        """
        current = int(self.currentime.strftime("%H%M"))
        return {
            current in range(700, 730): "700",
            current in range(730, 800): "730",
            current in range(800, 830): "800",
            current in range(830, 900): "830",
            current in range(900, 930): "900",
            current in range(930, 1000): "930",
            current in range(1000, 1030): "1000",
            current in range(1030, 1100): "1030",
            current in range(1100, 1130): "1100",
            current in range(1130, 1200): "1130",
            current in range(1200, 1230): "1200",
            current in range(1230, 1300): "1230",
            current in range(1300, 1330): "1300",
            current in range(1330, 1400): "1330",
            current in range(1400, 1430): "1400",
            current in range(1430, 1500): "1430",
            current in range(1500, 1530): "1500",
            current in range(1530, 1600): "1530",
            current in range(1600, 1630): "1600",
            current in range(1630, 1700): "1630",
            current in range(1700, 1730): "1700",
            current in range(1730, 1800): "1730",
            current in range(1800, 1830): "1800",
            current in range(1830, 1900): "1830",
            current in range(1900, 1930): "1900",
            current in range(1930, 2000): "1930",
            current in range(2000, 2030): "2000",
            current in range(2030, 2100): "2030",
            current in range(2100, 2130): "2100",
            current in range(2130, 2200): "2130",
            current in range(2200, 2230): "2200",
            current in range(2230, 2300): "2230",
            current in range(2300, 2330): "2300",
            current in range(2330, 2400): "2330",
        }.get(True, "0")

    def brightness(self):
        """
        Returns: El valor actual del brillo en multiplo de 5.
        """
        return str(round(self.screen.Brightness / 5) * 5)
