import os
import shutil
from datetime import datetime, timedelta

# Define the path to the directory to organize
path = "C:/Users/micah/Downloads/_Seminar 03 - Documentation book/"

# Define the names of the folders to create and their associated file extensions

folders = {
    "Current": set(),
    "Documents": {".doc", ".docx", ".txt", ".md", ".opml", ".tex", ".bib"},
    "Presentations": {".ppt", ".pptx", ".key", ".odp"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"},
    "Vector Graphics": {".ai", ".eps"},
    "pdfs": {".pdf"},
    "Raster Graphics": {".psd", ".raw", ".cr2", ".nef", ".orf", ".sr2"},
    "Video": {".avi", ".mp4", ".mov", ".wmv", ".mkv", ".flv", ".webm", ".mpg", ".mpeg", ".3gp"},
    "Audio": {".mp3", ".wav", ".m4a", ".aac", ".ogg", ".flac", ".wma"},
    "Code": {".py", ".ipynb", ".java", ".cpp", ".c", ".h", ".cs", ".xml", ".json", ".yaml", ".yml", ".sql", ".rb", ".pl", ".sh", ".bat", ".cmd", ".ps1", ".dockerfile", ".fig", ".js"},
    "Web Files": {".html", ".css", ".js", ".php"},
    "Database": {".sqlite", ".db", ".sql", ".kdbx"},
    "Executable Files": {".exe", ".msi", ".deb", ".dmg", ".appimage", ".sh", ".apk", ".xpi"},
    "System Files": {".ini", ".cfg", ".plist", ".log", ".env", ".desktop", ".folder", ".flatpakref"},
    "Compressed Files": {".zip", ".tar", ".gz", ".7z", ".rar", ".deb", ".rpm"},
    "Disk Images": {".iso", ".img", ".vmdk"},
    "Other": {".tid", ".vcf"},
    "Miscellaneous": set()
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
