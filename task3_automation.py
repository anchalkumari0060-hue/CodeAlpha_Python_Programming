import os
import shutil

source_folder = input("Enter source folder path: ").strip()
destination_folder = input("Enter destination folder path: ").strip()

if not os.path.exists(source_folder):
    print("Source folder does not exist.")
    exit()

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

count = 0

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        old_path = os.path.join(source_folder, file)
        new_path = os.path.join(destination_folder, file)

        shutil.move(old_path, new_path)
        print(file, "moved successfully.")
        count += 1

print("\nTask completed.")
print("Total JPG files moved:", count)
