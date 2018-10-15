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
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    n = 0
    new_index = 0
    while n == 0:
        for index, character in enumerate(new_name):
            index = index + new_index
            if (index == len(new_name) - 1):
                n = 1
            elif (index >= 1) and (new_index < len(new_name)-1):
                previous_character = new_name[index - 1]
                current_character = character
                next_character = new_name[index + 1]
                conditionbase1 = current_character.isupper() is True and previous_character.islower() is True and next_character.islower() is True
                conditionbase2 = current_character.islower() is True and previous_character.islower() is True and next_character.isupper() is True
                conditionbase3 = current_character.isupper() is True and previous_character.isupper() is True and next_character.islower() is True
                conditionbase4 = current_character.islower() is True and previous_character.islower() is True and next_character.isupper() is True
                conditiondashcur = current_character == '_'
                conditiondashprev = previous_character == '_'
                conditiondashnext = next_character == '_'
                conditiondot = current_character == '.'
                if conditionbase1 is True and conditiondashprev is False:
                    new_name = new_name.replace(new_name[index], '_{}'.format(current_character), 1)
                    new_name = new_name
                    new_index = 1
                elif conditionbase2 is True and conditiondashprev is False:
                    new_name = new_name.replace(new_name[index], '{}_'.format(current_character), 1)
                    new_name = new_name
                    new_index = 1

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

