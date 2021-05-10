import os
from pathlib import Path
from uuid import uuid4

path = str(Path.cwd())

# if storage doesn't exist then create it
if not os.path.exists('{}/storage'.format(path)):
    os.mkdir('{}/storage'.format(path))

root_path = '{}/storage/'.format(path)


# return file name
def handle_upload_file(file) -> str:
    file_name = str(file)
    file_path = root_path + file_name

    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path


def write_input(text: str) -> str:
    file_name = str(uuid4()) + '.txt'
    file_path = root_path + file_name

    with open(file_path, 'w+') as file:
        file.write(text)
    return file_path
