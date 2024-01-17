import os
import shutil

def move_files_based_on_name(source_folder, destination_folder):
    # Check and create folders in destination
    cover_letters_folder = os.path.join(destination_folder, "Cover Letters")
    cv_folder = os.path.join(destination_folder, "CV")

    if not os.path.exists(cover_letters_folder):
        os.makedirs(cover_letters_folder)
    
    if not os.path.exists(cv_folder):
        os.makedirs(cv_folder)

    # Scan through files in the source folder
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        file_name = file.lower()  # Convert to lower case for case-insensitive comparison

        # Check for specific keywords and move the file
        if "cover letter" in file_name:
            shutil.move(file_path, cover_letters_folder)
            print(f"Moved '{file}' to 'Cover Letters'")
        elif "clément douale" in file_name or "clement douale" in file_name:
            shutil.move(file_path, cv_folder)
            print(f"Moved '{file}' to 'CV'")

# Define source and destination folders
downloads_folder = os.path.expanduser('~/Downloads')
documents_folder = os.path.expanduser('~/Documents')

# Move files based on their names
move_files_based_on_name(downloads_folder, documents_folder)
