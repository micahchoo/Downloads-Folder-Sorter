![https://ailabels.org/#made-primarily-by-ai](https://github.com/micahchoo/Downloads-Folder-Sorter/blob/67de0678def24e5754947f59565ed96620e5144d/AI%20Labels%20-%20AI.svg)

# Introduction

This File and Folder Sorter is a Python program that organizes files in a specified directory into folders based on their file extensions. It is useful for individuals who have a cluttered downloads folder or other directories with a variety of file types. It sorts any type of files into their respective Folders based on date or use-case. Helps those who have a lot of files to manage. You can modify this folder classification according to your specific use case by adding or removing file extensions within each category to better suit your needs as a doctor, designer, or any other use-case. 


## Requirements

The File Organizer requires Python 3.5 or higher to be installed on your computer.

## Installation

   - Download the program code from the Github repository.
   - Extract the files to a directory of your choice.

## Usage

   - Open the organize_files.py file in a Python editor of your choice.
   - Edit the path variable to specify the directory containing the files you want to organize.
   - Edit the folders dictionary to add or remove folders and their associated file extensions as needed.
   - Save the changes to the organize_files.py file.
   - Run the organize_files.py file.
  
 The program will automatically move files in the specified directory to their corresponding folders based on their file extensions. Do it on a Test Directory first. 

# Customization

1. If you would like to customize the program for your own needs, you can edit the folders dictionary to add or remove folders and their associated file extensions as needed. this repository uses this classification. 

```python
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
```
2. You can also change the time threshold for file organization by editing the threshold variable.


```python
# Set the time threshold to 90 days ago
threshold = timedelta(days=30)
```


# Troubleshooting

If you encounter any issues with the program, please check the following:

  -  Make sure that you have Python 3.5 or higher installed on your computer.
  -  Make sure that you have edited the path variable to specify the correct directory containing the files you want to organize.
    - Path directory may look different on different OSs. Make sure your path has forward slashes
  -  Make sure that you have edited the folders dictionary to add or remove folders and their associated file extensions as needed.
  -  Make sure that you have saved the changes to the organize_files.py file before running the program.

