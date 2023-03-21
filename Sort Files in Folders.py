# Check if the folder names from the `folders` dictionary are already present
for folder_name, extensions in folders.items():
    # Create the folder for the extension if it does not exist
    if not os.path.exists(os.path.join(path, folder_name)):
        os.makedirs(os.path.join(path, folder_name))
    else:
        continue
    
# Create the Folders folder if it doesn't exist
folders_folder = os.path.join(path, "Folders")
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
                    # Skip the Miscellaneous folder
                    if folder_name == "Miscellaneous":
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
        # If it's a folder, move it to the Old_Folders folder
        elif os.path.isdir(filepath):
            folder_path = os.path.join(path, "Folders", "Old_Folders")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(filepath, os.path.join(folder_path, filename))
    # If it is not older than the threshold, go to the next file
    else:
        continue
