#! /usr/bin/env python3
import argparse
import os
from src import file_service


def read_file():
    filename = input("Enter file name : ")
    print(file_service.read_file(filename))


def create_file():
    content = input("Enter file content : ")
    file = file_service.create_file(content)
    print(f'New file was created: {file}')


def delete_file():
    filename = input("Enter file name : ")
    file = file_service.delete_file(filename)
    print(f'This file was deleted: {file}')


def list_dir():
    print(file_service.list_dir())


def change_dir():
    directory = input("Enter dir name : ")
    new_directory = file_service.change_dir(directory)
    print(f'Working directory is {new_directory} now')


def get_file_permissions():
    filename = input("Enter file name: ")
    permissions = file_service.get_file_permissions(filename)
    print(f"File {filename} permissions: {permissions}")


def set_file_permissions():
    filename = input("Enter file name : ")
    permissions = input("Input UNIX permissions in oct format :")
    new_permissions = file_service.set_file_permissions(filename, permissions)
    print(f"Set {new_permissions} to {filename}")


def main():
    parser = argparse.ArgumentParser(description='Restfull file server')
    parser.add_argument('-d', '--directory', help='Working directory', default='./')
    args = parser.parse_args()
    os.chdir(args.directory)
    print(f'Working directory is {os.getcwd()}')
    commands = {
        "read": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir,
        "gmod": get_file_permissions,
        "chmod": set_file_permissions
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution: {ex} ")


if __name__ == "__main__":
    main()
