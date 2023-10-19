import os
import sys
import time
import shutil
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pyautogui

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    path = '/Volumes'
    main_destination_directory = '/Users/nico.rupprecht/Desktop/01_Ingest'
    backup_directory = '/Users/nico.rupprecht/Desktop/02_Backup'
    project_file_path = '/Users/nico.rupprecht/Desktop'

class CustomEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        volume_name = os.path.basename(event.src_path)
        if 'KAM_A' in volume_name:
            print(f'VOLUME inserted: {volume_name}')
            time.sleep(2)
            source_path = os.path.join(path, volume_name)
            main_destination_path = os.path.join(main_destination_directory, volume_name)
            backup_destination_path = os.path.join(backup_directory, volume_name)
            try:
                shutil.copytree(source_path, main_destination_path, ignore=shutil.ignore_patterns('*.pyc', 'tmp*', ".*"))
                os.chmod(main_destination_path, 0o777)
                print(f'VOLUME: "{volume_name}" copied to {backup_destination_path}')
                self.print_copied_contents(main_destination_path)
            except Exception as e:
                print(f'ERROR: {str(e)}')

            try:
                shutil.copytree(source_path, backup_destination_path, ignore=shutil.ignore_patterns('*.pyc', 'tmp*', ".*"))
                os.chmod(backup_destination_path, 0o777)
                print(f'VOLUME: "{volume_name}" copied to {backup_destination_path}')
                self.print_copied_contents(backup_destination_path)
            except Exception as e:
                print(f'ERROR: {str(e)}')
            
            time.sleep(2)
            self.create_premiere_pro_project(volume_name)

    def print_copied_contents(self, destination_path):
        for root, dirs, files in os.walk(destination_path):
            for name in files:
                file_path = os.path.join(root, name)
                print(f'--- File: "{name}" copied to {file_path}')
            for name in dirs:
                dir_path = os.path.join(root, name)
                print(f'--- Directory: "{name}" copied to path: {dir_path}')
                
                
    def create_premiere_pro_project(self, volume_name):
    # Wait for Premiere Pro to open (adjust the path based on your system)
        premiere_pro_path = "/Applications/Adobe Premiere Pro 2023/Adobe Premiere Pro 2023.app"
        subprocess.Popen(["open", premiere_pro_path])
        time.sleep(30)
        pyautogui.hotkey("n")
        time.sleep(2)
        pyautogui.hotkey('option', 'command', 'n')
        time.sleep(2)
        pyautogui.write("TEST")
        time.sleep(2)
        pyautogui.press('enter')

        print("Premiere Pro project created.")

                    
event_handler = CustomEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()







# import os
# import sys
# import time
# import shutil
# import logging
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')

#     # Set the path to the /Volumes directory
#     path = '/Volumes'

#     # Set the destination directory for the main copy operation
#     main_destination_directory = '/Users/ufapost/Downloads/ShootingDay_X/Main'  # Replace with your desired destination directory

#     # Set the backup directory
#     backup_directory = '/Users/ufapost/Downloads/ShootingDay_X/Backup'  # Replace with your desired backup directory

#     class CustomEventHandler(FileSystemEventHandler):
#         def on_created(self, event):
#             volume_name = os.path.basename(event.src_path)
#             if 'SETUP' in volume_name:
#                 print(f'Volume created: {volume_name}')
#                 time.sleep(5)
#                 # Perform the main copy operation using shutil.copytree
#                 source_path = os.path.join(path, volume_name)
#                 main_destination_path = os.path.join(main_destination_directory, volume_name)
#                 backup_destination_path = os.path.join(backup_directory, volume_name)
#                 try:
#                     shutil.copytree(source_path, main_destination_path)
#                     os.chmod(main_destination_path, 0o777)  # Adjust permissions as needed
#                     print(f'Contents of {volume_name} copied to {main_destination_path}')
#                 except Exception as e:
#                     print(f'Error copying contents of {volume_name} to {main_destination_path}: {str(e)}')

#                 try:
#                     shutil.copytree(source_path, backup_destination_path)
#                     os.chmod(backup_destination_path, 0o777)  # Adjust permissions as needed
#                     print(f'Contents of {volume_name} copied to {backup_destination_path}')
#                 except Exception as e:
#                     print(f'Error copying contents of {volume_name} to {backup_destination_path}: {str(e)}')
#     event_handler = CustomEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()

#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()






 
# import os
# import sys
# import time
# import shutil
# import logging
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
    
#     # Set the path to the /Volumes directory
#     path = '/Volumes'
    
#     # Set the destination directory for the copy operation
#     destination_directory = '/Users/ufapost/Downloads'  # Replace with your desired destination directory
    
#     class CustomEventHandler(FileSystemEventHandler):
#         def on_created(self, event):
#             volume_name = os.path.basename(event.src_path)
#             if 'SETUP' in volume_name:
#                 print(f'Volume created: {volume_name}')
#                 time.sleep(5) 
#                 # Perform the copy operation using shutil.copytree
#                 source_path = os.path.join(path, volume_name)
#                 destination_path = os.path.join(destination_directory, volume_name)
#                 try:
#                     shutil.copytree(source_path, destination_path)
                    
#                     # Set permissions for the destination directory (readable and writable)
#                     os.chmod(destination_path, 0o777)  # Adjust permissions as needed
                    
#                     print(f'Contents of {volume_name} copied to {destination_path}')
#                 except Exception as e:
#                     print(f'Error copying contents of {volume_name}: {str(e)}')

#     event_handler = CustomEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
    
#     try:
#         while True:
#             time.sleep(1)
#     finally:
#         observer.stop()
#         observer.join()
