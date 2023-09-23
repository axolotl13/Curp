"""
Copyright (c) 2023 Geovanni Santamaria. All Rights Reserved.
"""
import json
from datetime import datetime
from pathlib import Path

from pydbus import SessionBus


class Brightness:
    """
    Attributes:
        screen: Usa la librería pydbus para cambiar el valor del brillo.
        logfile: Ruta que usa para almacenar los valores del brillo.
    """

    json_file = Path("/tmp/datos.json")

    def __init__(self) -> None:
        bus = SessionBus()
        self.screen = bus.get("org.gnome.SettingsDaemon.Power")[".Screen"]
        if not self.json_file.exists():
            self.json_file.touch()

    def timeformat(self) -> str:
        """
        Guarda el valor en el archivo especifico segun la hora.
        Retorna el valor si la hora cumple con el rango establecido.
        """
        logfile = self.json_file
        data = json.loads(logfile.read_text())

        current = int(datetime.now().strftime("%H%M"))
        return {
            current in range(700, 730): data.get("700"),
            current in range(730, 800): data.get("730"),
            current in range(800, 830): data.get("800"),
            current in range(830, 900): data.get("830"),
            current in range(900, 930): data.get("900"),
            current in range(930, 1000): data.get("930"),
            current in range(1000, 1030): data.get("1000"),
            current in range(1030, 1100): data.get("1030"),
            current in range(1100, 1130): data.get("1100"),
            current in range(1130, 1200): data.get("1130"),
            current in range(1200, 1230): data.get("1200"),
            current in range(1230, 1300): data.get("1230"),
            current in range(1300, 1330): data.get("1300"),
            current in range(1330, 1400): data.get("1330"),
            current in range(1400, 1430): data.get("1400"),
            current in range(1430, 1500): data.get("1430"),
            current in range(1500, 1530): data.get("1500"),
            current in range(1530, 1600): data.get("1530"),
            current in range(1600, 1630): data.get("1600"),
            current in range(1630, 1700): data.get("1630"),
            current in range(1700, 1730): data.get("1700"),
            current in range(1730, 1800): data.get("1730"),
            current in range(1800, 1830): data.get("1800"),
            current in range(1830, 1900): data.get("1830"),
            current in range(1900, 1930): data.get("1900"),
            current in range(1930, 2000): data.get("1930"),
            current in range(2000, 2030): data.get("2000"),
            current in range(2030, 2100): data.get("2030"),
            current in range(2100, 2130): data.get("2100"),
            current in range(2130, 2200): data.get("2130"),
            current in range(2200, 2230): data.get("2200"),
            current in range(2230, 2300): data.get("2230"),
            current in range(2300, 2330): data.get("2300"),
            current in range(2330, 2400): data.get("2330"),
        }.get(True, "0")

    def brightness(self) -> int:
        """
        Returns: El valor actual del brillo en multiplo de 5.
        """
        return round(self.screen.Brightness / 5) * 5
