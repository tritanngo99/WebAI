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

    origin_name = str(file)

    file_extensions = ['.py', '.c', '.cpp', '.java']
    file_extension = ''

    for extension in file_extensions:
        if origin_name.endswith(extension):
            file_extension = extension
            break
    print(file_extension)
    # file extension invalid
    if file_extension == '':
        return None

    file_name = str(uuid4()) + file_extension

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
