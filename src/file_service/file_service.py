import os
from src import utils
from src import crypto


def _read_signed_file(filename, data):
    for label in crypto.SignatureFactory.signers:
        sig_filename = f'{filename}.{label}'
        if os.path.exists(sig_filename):
            signer = crypto.SignatureFactory.get_signer(label)
            with open(sig_filename, 'r') as sig_file:
                actual_sig = signer(data)
                expected_sig = sig_file.read()
                if actual_sig == expected_sig:
                    return data
                else:
                    raise Exception('File broken')


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    checked_data = _read_signed_file(filename, data)
    return checked_data


def _create_signed_file(content, filename, label='md5'):
    sig_filename = f'{filename}.{label}'
    signer = crypto.SignatureFactory.get_signer(label)
    sig_content = signer(content)
    with open(sig_filename, "w") as f:
        f.write(sig_content)


def create_file(content):
    filename = utils.random_string_and_number()+'.txt'
    while filename in os.listdir():
        filename = utils.random_string_and_number()
    with open(f"{filename}", "w") as f:
        f.write(content)
    _create_signed_file(content, filename)
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
