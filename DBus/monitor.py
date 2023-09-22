from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from dbusmain import main


class Monitor(FileSystemEventHandler, main):
    def on_modified(self, event):
        super().on_modified(event)
        return self.write_file()

    def write_file(self):
        brightness = self.getTimeValue()
        default_file = open(self.logfile.joinpath(brightness), "w")
        default_file.write(self.getBrightnessValue())
        default_file.close()


def run():
    path = Monitor().path
    event_handler = Monitor()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


run()
