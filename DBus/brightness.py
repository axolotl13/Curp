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
        json_file: Archivo donde se almacenan los datos.
        screen: Usa la librería pydbus para cambiar el valor del brillo del sistema.
    """

    def __init__(self) -> None:
        bus = SessionBus()

        self.json_file = Path("~/.config/data.json").expanduser()
        self.screen = bus.get("org.gnome.SettingsDaemon.Power")[".Screen"]
        if not self.json_file.exists():
            self.json_file.touch()
            self.json_file.write_text("{}", encoding="UTF-8")

    def timeformat(self) -> str:
        """
        Returns: Tomá la hora actual, si los minutos son menor a la media hora,
        la hora queda como h:00 del caso contrario h:30.
        """
        current_date = datetime.now()
        minutes = int(current_date.strftime("%M"))
        hours = current_date.strftime("%H")
        current_time = hours + "00" if minutes < 30 else hours + "30"
        return current_time

    def json_data(self) -> dict:
        """
        Returns: Lee un archivo json.
        """
        logfile = self.json_file
        data = json.loads(logfile.read_text(encoding="UTF-8"))
        return data

    def brightness(self) -> int:
        """
        Returns: Tomá el valor del brillo actual y lo convierte en multiplo de 5.
        """
        return round(self.screen.Brightness / 5) * 5
