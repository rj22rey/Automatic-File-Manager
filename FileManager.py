import os
import shutil
from datetime import datetime
import json

# Define file categories
FILE_CATEGORIES = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'],
    'documents': ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt'],
    'videos': ['mp4', 'avi', 'mov', 'mkv', 'flv'],
    'audio': ['mp3', 'wav', 'aac', 'ogg'],
    'archives': ['zip', 'rar', 'tar', 'gz'],
    'scripts': ['py', 'js', 'html', 'css'],
    'others': []  # For files that do not fit into the predefined categories
}

def get_file_category(extension):
    """Determine the category of a file based on its extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'others'

def organize_folder():
    folder_path = os.getcwd()  # Use the current working directory
    original_locations = {}

    backup_folder = os.path.join(folder_path, "backup")
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if os.path.isfile(item_path):
            file_type = item.split('.')[-1]
            category = get_file_category(file_type)
            mod_time = os.path.getmtime(item_path)
            mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m')

            # Create folder structure based on category and modification date
            new_folder = os.path.join(folder_path, category, mod_date)
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            new_path = os.path.join(new_folder, item)

            # Move the file to the new folder and save the original location
            shutil.move(item_path, new_path)
            original_locations[new_path] = item_path

    # Save the original locations to a file for undo functionality
    with open(os.path.join(backup_folder, 'original_locations.json'), 'w') as f:
        json.dump(original_locations, f)

def undo_changes():
    folder_path = os.getcwd()  # Use the current working directory
    backup_folder = os.path.join(folder_path, "backup")
    original_locations_file = os.path.join(backup_folder, 'original_locations.json')

    if not os.path.exists(original_locations_file):
        print("No backup found to undo changes.")
        return

    with open(original_locations_file, 'r') as f:
        original_locations = json.load(f)

    # Move files back to their original locations
    for new_path, original_path in original_locations.items():
        shutil.move(new_path, original_path)

    # Remove the backup folder
    shutil.rmtree(backup_folder)

def main():
    while True:
        action = input("Enter 'organize' to organize files, 'undo' to undo changes, or 'exit' to quit: ").strip().lower()
        if action == 'exit':
            break

        if action == 'organize':
            organize_folder()
            print("Files organized successfully.")
        elif action == 'undo':
            undo_changes()
            print("Changes have been undone.")
        else:
            print("Invalid action. Please enter 'organize', 'undo', or 'exit'.")

if __name__ == "__main__":
    main()
