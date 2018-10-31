"""
CP1404 Practical 9 - Ryan Honorica
"""
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    filename = filename.replace('.TXT', '.txt')
    new_name = ""
    for index, current_character in enumerate(filename):
        if current_character.isupper() and index != 0:
            new_name += '_'
        elif current_character == ' ':
            new_name += '_'
        else:
            new_name += current_character
    new_name = '_'.join([name.title() for name in new_name.split('_')])
    new_name = new_name.replace('.Txt', '.txt')
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics/Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for name in filenames:
            complete_name = os.path.join(directory_name, name)
            new_name = os.path.join(directory_name, get_fixed_filename(name))
            os.rename(complete_name, new_name)


main()

