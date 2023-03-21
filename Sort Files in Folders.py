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
    "Miscellaneous": set(),
    "Old_Folders": set(),
    "Meta": {" "}
}

# Check if the folder names from the `folders` dictionary are already present
for folder_name, extensions in folders.items():
    # Skip the Miscellaneous and Old_Folders folders
    if folder_name in {"Miscellaneous", "Old_Folders"}:
        continue
    # Create the folder for the extension if it does not exist
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))

# Create the Miscellaneous and Old_Folders folders if they don't exist
for folder_name in ["Miscellaneous", "Old_Folders"]:
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))
        
# Set the time threshold to 90 days ago
threshold = timedelta(days=30)

# Loop over all files in the path
for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    # Check if it is older than the threshold
    file_modification_time = datetime.fromtimestamp(os.path.getmtime(filepath))
    if datetime.now() - file_modification_time <= threshold:
        continue
    
    if os.path.isfile(filepath):
        # If it's a file, determine its extension
        ext = os.path.splitext(filename)[1]
        folder_name = None
        # Find the folder that corresponds to the extension
        for name, extensions in folders.items():
            if name in {"Miscellaneous", "Old_Folders"}:
                continue
            if ext in extensions:
                folder_name = name
                break
        # If the extension is not in any of the folders in the dictionary, move it to the Miscellaneous folder
        if folder_name is None:
            folder_name = "Miscellaneous"
        # Move the file to the appropriate folder
        folder_path = os.path.join(path, folder_name)
        shutil.move(filepath, os.path.join(folder_path, filename))
        
    elif os.path.isdir(filepath) and filename not in folders:
        # If it's a folder and not in the 'folders' dictionary, move it to the Old_Folders folder
        shutil.move(filepath, os.path.join(path, "Old_Folders", filename))
