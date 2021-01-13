import os
import shutil


def copying(path, target_path, type_to_copy):
    """Copying files to a new repository"""
    for file in os.listdir():
        name, extension = os.path.splitext(file)
        if extension in type_to_copy:
            shutil.copy(path + "\\" + file, target_path)
            os.remove(path + "\\" + file)
    print("Сopying completed!")


def run():
    """Program launch"""
    path = input("Enter the path to the files: ")
    try:
        os.chdir(path)
    except FileNotFoundError:
        return run()
    target_path = input("Enter a new path for files if it does not already exist the program will create it: ")
    try:
        os.mkdir(target_path)
    except OSError:
        pass
    type_to_copy = input("Enter the format(s) of dotted file to be transferred (separated by ';'): ").split(";")
    return copying(path, target_path, type_to_copy)


run()
