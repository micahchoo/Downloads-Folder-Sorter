import os
import shutil
from datetime import datetime, timedelta

# Define the path to the directory to organize
dir_path = "/path/to/directory"

# Define the names of the folders to create and their associated file extensions
folders = {
    "Current": set(),
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"},
    "Videos": {".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv"},
    "Music": {".mp3", ".wav", ".flac", ".aac", ".m4a"},
    "Archives": {".zip", ".rar", ".tar", ".gz"},
    "Miscellaneous": set()
}

# Define the time threshold for moving files to the Current folder
current_threshold = datetime.now() - timedelta(days=90)

# Organize the files
for filename in os.listdir(dir_path):
    filepath = os.path.join(dir_path, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        if ext in folders["Current"]:
            shutil.move(filepath, os.path.join(dir_path, "Current", filename))
        elif ext in folders["Miscellaneous"]:
            shutil.move(filepath, os.path.join(dir_path, "Miscellaneous", filename))
        else:
            found = False
            for folder, exts in folders.items():
                if folder == "Current" or folder == "Miscellaneous":
                    continue
                if ext in exts:
                    shutil.move(filepath, os.path.join(dir_path, folder, filename))
                    found = True
                    break
            if not found and os.path.getctime(filepath) >= current_threshold:
                shutil.move(filepath, os.path.join(dir_path, "Current", filename))
