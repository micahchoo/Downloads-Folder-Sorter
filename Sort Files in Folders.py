import os
import shutil
from datetime import datetime, timedelta

# Define the path to the directory to organize
path = "C:/Users/micah/Downloads/_Seminar 03 - Documentation book/"

# Define the names of the folders to create and their associated file extensions
folders = {
    "Documents": {".doc", ".docx", ".txt", ".md", ".opml", ".tex", ".bib"},
    "Presentations": {".ppt", ".pptx", ".key", ".odp"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"},
    "Vector Graphics": {".ai", ".eps"},
    #"pdfs": {".pdf"},
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
    "Miscellaneous": set(),
    "Old_Folders": set()
}

# Check if the folder names from the `folders` dictionary are already present
for folder_name, extensions in folders.items():
    # Create the folder for the extension if it does not exist
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))
    else:
        continue
    
# Create the Folders folder if it doesn't exist
folders_folder = os.path.join(path, "Old_Folders")
if not os.path.exists(folders_folder):
    os.makedirs(folders_folder)

# Set the time threshold to 90 days ago
threshold = timedelta(days=90)

# Loop over all files in the path
for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    # Check if it is older than the threshold
    file_modification_time = datetime.fromtimestamp(os.path.getmtime(filepath))
    if datetime.now() - file_modification_time < threshold:
        # If it's a file, determine its extension
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1]
            # If the extension is in the dictionary, move the file to the appropriate folder
            if ext in folders:
                found = False
                for folder_name, extensions in folders.items():
                    # Skip the Miscellaneous and folders from the 'folders' dictionary
                    if folder_name == "Miscellaneous" or folder_name in folders:
                        continue
                    # Check if the extension is in the list for this folder
                    if ext in extensions:
                        # Move the file to the appropriate folder
                        folder_path = os.path.join(path, folder_name)
                        shutil.move(filepath, os.path.join(folder_path, filename))
                        found = True
                        break
                # If the extension is not in any of the folders in the dictionary, move it to the Miscellaneous folder
                if not found:
                    shutil.move(filepath, os.path.join(path, "Miscellaneous", filename))
            # If the extension is not in the dictionary, move it to the Miscellaneous folder
            else:
                shutil.move(filepath, os.path.join(path, "Miscellaneous", filename))
        # If it's a folder and not in the 'folders' dictionary, move it to the Old_Folders folder
        elif os.path.isdir(filepath) and filename not in folders:
            shutil.move(filepath, os.path.join(path, "Old_Folders", filename))
    # If it is not older than the threshold, go to the next file
    else:
        continue
