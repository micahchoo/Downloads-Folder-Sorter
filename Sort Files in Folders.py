import os
import shutil
import datetime


# Path of the directory to be organized - i used this as a test bed
path = "C:/Users/micah/Downloads/_Seminar 03 - Documentation book/"

# Date range for files to be moved to Current folder
current_date = datetime.datetime.now()
three_months_ago = current_date - datetime.timedelta(days=90)



# List of extensions and their corresponding folder names
extensions = {
    '.png': 'Images',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.eps': 'Images',
    '.raw': 'Images',
    '.cr2': 'Images',
    '.nef': 'Images',
    '.orf': 'Images',
    '.sr2': 'Images',
    '.txt': 'Text Files',
    '.doc': 'Text Files',
    '.docx': 'Text Files',
    '.log': 'Text Files',
    '.ppt': 'Presentation',
    '.pptx': 'Presentation',
    '.csv': 'Data Files',
    '.key': 'Data Files',
    '.keychain': 'Data Files',
    '.dat': 'Data Files',
    '.sdf': 'Data Files',
    '.tar': 'Data Files',
    '.xml': 'Data Files',
    '.vcf': 'Data Files',
    '.aif': 'Music',
    '.iff': 'Music',
    '.m3u': 'Music',
    '.m4a': 'Music',
    '.mid': 'Music',
    '.mp3': 'Music',
    '.mpa': 'Music',
    '.wav': 'Music',
    '.wma': 'Music',
    '.3g2': 'Videos',
    '.3gp': 'Videos',
    '.asf': 'Videos',
    '.avi': 'Videos',
    '.flv': 'Videos',
    '.m4v': 'Videos',
    '.mov': 'Videos',
    '.mp4': 'Videos',
    '.mpg': 'Videos',
    '.rm': 'Videos',
    '.zip': 'Compressed Files',
    '.rar': 'Compressed Files',
    '.7z': 'Compressed Files',
    '.bz2': 'Compressed Files',
    '.gz': 'Compressed Files',
    '.tar.gz': 'Compressed Files',
    '.dmg': 'Disk Image Files',
    '.iso': 'Disk Image Files',
    '.exe': 'Executables',
    '.jar': 'Executables',
    '.msi': 'Executables',
    '.deb': 'Executables',
    '.dll': 'System Files',
    '.sys': 'System Files',
    '.cfg': 'Settings Files',
    '.ini': 'Settings Files',
    '.json': 'Settings Files',
    '.plist': 'Settings Files',
    '.bak': 'Misc Files',
    '.tmp': 'Misc Files',
    '.crdownload': 'Misc Files',
    '.part': 'Misc Files',
    '': 'Misc Files',
    '.apk': 'Android App Package',
    '.bib': 'Data Files',
    '.html': 'Web Files',
    '.css': 'Web Files',
    '.fig': '3D',
    '.folder': 'System Files',
    '.flatpakref': 'System Files',
    '.webp': 'Images',
    '.js': 'Web Files',
    '.json': 'Data Files',
    '.kdbx': 'Database',
    '.md': 'Text Files',
    '.opml': 'Text Files',
    '.py': 'Developer Files',
    '.svg': 'Images',
    '.tid': 'Data Files',
    '.vcf': 'Data Files',
    '.xml': 'Data Files',
    '.xpi': 'System Files'
}
# Create Current folder if it doesn't exist
current_folder = os.path.join(path, "Current")
if not os.path.exists(current_folder):
    os.makedirs(current_folder)

# Create folders for the extensions
for folder_name in extensions.values():
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files created within the last 3 months to Current folder
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        if file_creation_time >= three_months_ago:
            shutil.move(file_path, os.path.join(current_folder, file_name))

# Move files older than 3 months to their respective folders
for file_name in os.listdir(path):
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file_name)[1]
        folder_name = extensions.get(file_ext, 'Misc Files')
        folder_path = os.path.join(path, folder_name)
        shutil.move(file_path, os.path.join(folder_path, file_name))
