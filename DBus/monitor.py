"""
Copyright (c) 2023 Geovanni Santamaria. All Rights Reserved.
"""
import json
from datetime import datetime

from brightness import Brightness
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class Monitor(FileSystemEventHandler, Brightness):
    def on_modified(self, event):
        if event.is_directory:
            return

        # with open(self.json_file, "r") as json_file:
        #     data = json.load(json_file)
        data = self.timeformat()
        data[self.current_time] = self.brightness()
        with open(self.json_file, "w") as json_file:
            json.dump(data, json_file)
        # currentime_file = self.logs / self.timeformat()
        # if not currentime_file.exists():
        #     currentime_file.touch()
        # currentime_file.write_text(self.brightness())


path = "/sys/class/backlight/amdgpu_bl1/brightness"

event_handler = Monitor()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()
