import os
import random

class FolderManager:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self._create_folder_if_not_exists()

    def _create_folder_if_not_exists(self):
        # Create the folder if it doesn't exist
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
    
    def create_files(self, number_of_files):
        # Step 2: Create a number of files inside the folder
        for i in range(1, number_of_files + 1):
            file_path = os.path.join(self.folder_path, f'file_{i}.txt')
            with open(file_path, 'w') as file:
                file.write(f'This is file number {i}')
        print(f"{number_of_files} files created.")

    def count_files(self):
        # Step 3: Check the length of files in that folder
        files = os.listdir(self.folder_path)
        file_count = len([f for f in files if os.path.isfile(os.path.join(self.folder_path, f))])
        print(f"Number of files in the folder: {file_count}")
        return file_count

    def delete_random_half(self):
        # Step 4: Delete random half of the files in the folder
        files = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
        half_count = len(files) // 2
        files_to_delete = random.sample(files, half_count)

        for file in files_to_delete:
            os.remove(os.path.join(self.folder_path, file))
        
        print(f"{half_count} files deleted randomly.")
    
    def check_result(self):
        # Step 5: Check the result after deletion
        remaining_files = os.listdir(self.folder_path)
        remaining_file_count = len([f for f in remaining_files if os.path.isfile(os.path.join(self.folder_path, f))])
        print(f"Number of files remaining in the folder: {remaining_file_count}")
        return remaining_file_count

# Example usage:

# Initialize the FolderManager with a folder path
folder_path = 'example_folder'
folder_manager = FolderManager(folder_path)

# Create 10 files in the folder
folder_manager.create_files(10)

# Count the number of files in the folder
folder_manager.count_files()

# Delete random half of the files in the folder
folder_manager.delete_random_half()

# Check the number of files remaining
folder_manager.check_result()
