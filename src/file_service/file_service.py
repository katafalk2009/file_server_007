import os
from src import utils


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data


def create_file(content):
    filename = utils.random_string_and_number()
    if filename in os.listdir():
        raise Exception('This filename already exists')
    with open(f"{filename}.txt", "w") as f:
        f.write(content)
    return filename


def delete_file(filename):
    filename = os.path.abspath(filename)
    os.remove(filename)
    return filename


def list_dir():
    list_directory = os.listdir()
    return list_directory


def change_dir(directory):
    os.chdir(directory)
    return directory


def get_file_permissions(filename):
    permissions = oct(os.stat(filename).st_mode)
    return permissions


def set_file_permissions(filename, permissions):
    os.chmod(filename, int(permissions))
    return permissions
