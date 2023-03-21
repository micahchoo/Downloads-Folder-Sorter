import os
import shutil
from datetime import datetime, timedelta

# Define the path to the directory to organize
path = "C:/Users/micah/Downloads/_Seminar 03 - Documentation book/"

# Define the names of the folders to create and their associated file extensions
folders = {
"Current": set(),
"Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".webp", ".svg"},
"Text Files": {".txt", ".doc", ".docx", ".log", ".md", ".opml"},
"Presentation": {".ppt", ".pptx"},
"Data Files": {".csv", ".key", ".keychain", ".dat", ".sdf", ".tar", ".xml", ".vcf", ".json", ".bib", ".tid"},
"Music": {".aif", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".wav", ".wma"},
"Videos": {".3g2", ".3gp", ".asf", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm"},
"Compressed Files": {".zip", ".rar", ".7z", ".bz2", ".gz", ".tar.gz"},
"Disk Image Files": {".dmg", ".iso"},
"Executables": {".exe", ".jar", ".msi", ".deb"},
"System Files": {".dll", ".sys", ".cfg", ".ini", ".plist", ".folder", ".flatpakref", ".xpi"},
"Database": {".kdbx"},
"Misc Files": {".bak", ".tmp", ".crdownload", ".part", ""},
"Android App Package": {".apk"},
"Web Files": {".html", ".css", ".js"}
}

# Create Current folder if it doesn't exist
current_folder = os.path.join(path, "Current")
if not os.path.exists(current_folder):
    os.makedirs(current_folder)

# Create folders for the extensions
for folder_name, extensions in folders.items():
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Define the time threshold for moving files to the Current folder
current_threshold = timedelta(days=90)

# Organize the files
for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1]
        if ext in folders["Current"]:
            shutil.move(filepath, os.path.join(current_folder, filename))
        elif ext in folders["Miscellaneous"]:
            shutil.move(filepath, os.path.join(path, "Miscellaneous", filename))
        else:
            found = False
            for folder_name, extensions in folders.items():
                if folder_name == "Current" or folder_name == "Miscellaneous":
                    continue
                if ext in extensions:
                    folder_path = os.path.join(path, folder_name)
                    shutil.move(filepath, os.path.join(folder_path, filename))
                    found = True
                    break
            if not found:
                file_creation_time = datetime.fromtimestamp(os.path.getctime(filepath))
                if file_creation_time + current_threshold < datetime.now():
                    shutil.move(filepath, os.path.join(current_folder, filename))
