
"""File Sorter Program to sort through the files of FilesToSort by Ryan Honorica"""
import os
import shutil


def main():
    sort_files('FilesToSort/FilesToSort')


def sort_files(folder_path):
    """Create new sub-folders depending on the file exstensions found to be common across the files."""
    files_to_sort = os.listdir(folder_path)
    file_types = []
    for file in os.listdir(folder_path):
        if not os.path.splitext(file)[1] in file_types:
            file_ext = os.path.splitext(file)[1]
            file_types.append(file_ext)
    for extension in file_types:
        new_directory = os.path.join(folder_path, extension[1:])
        os.mkdir(new_directory)
    for file in files_to_sort:
        directory = os.path.join(folder_path, file)
        destination = os.path.join(os.path.join(folder_path, os.path.splitext(file)[1][1:]))
        shutil.move(directory, destination, file)


main()
