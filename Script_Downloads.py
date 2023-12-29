# To make .exe file install pyinstaller by running command "pip install pyinstaller",
# After that through cmd navigate to script and run "pyinstaller --onefile Script_Downloads.py"
# To run script every day/week add it to Task Scheduler - Win + R type taskschd.msc enter
# Now click Create Basic Task, name it, locate .exe file of script, set date, save and enjoy
# Change current variable to your Downloads folder location for example : C:\\Users\\Downloads\\"
import os
import shutil
images = [".jpeg", ".png", ".jpg", ".gif"]  # Extensions for images
text = [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf"]  # Extensions for text files
videos = [".mp4", ".mkv", ".mov"]  # Extensions for videos
sounds = [".mp3", ".wav", ".m4a"]  # Extensions for sounds
applications = [".exe", ".lnk"]  # Extensions for applications
codes = [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php"]  # Extensions for codes

current = r"C:\Users\Desktop\Downloads"  # Source directory
files = os.listdir(current)  # List of files in the source directory

# Create folders based on the extension lists
for category_name, extensions in zip(["Images", "Text", "Videos", "Sounds", "Applications", "Codes"], [images, text, videos, sounds, applications, codes]):
    folder_path = os.path.join(current, category_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to their respective folders
for file in files:
    file_extension = os.path.splitext(file)[1].lower()

    for category_name, extensions in zip(["Images", "Text", "Videos", "Sounds", "Applications", "Codes"], [images, text, videos, sounds, applications, codes]):
        if file_extension in extensions:
            source_path = os.path.join(current, file)
            destination_folder = os.path.join(current, category_name)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            break

print("Files organized into folders based on their types.")