import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir =  "C:/Users/Lenovo/Downloads"
to_dir = "Downloaded_Files"

#event file handler class 
class FileEventHandler(FileSystemEventHandler):
     def on_Created(self,event):
      print(f"hey,{event.src_path} path has been created ")

     def on_modified(self, event):
          
          print(f" {event.src_path}your system has been modified")

     def on_moved(self,event):
        print(f"hey!,{event.src_path}moved")

     def on_deleted(self, event):
          print(f"oopse!,{event.src_path}the file has been deleted")



# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stop!!!")
    observer.stop()
