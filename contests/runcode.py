import os
from subprocess import check_output, STDOUT
from pathlib import Path
from uuid import uuid4

TIME_OUT = 2


def run_file_python(file: str, file_input: str) -> str:
    command = 'python3 {} < {}'.format(file, file_input)
    output = check_output(command, timeout=TIME_OUT, stderr=STDOUT, shell=True)
    output = output.strip()
    return output.decode()


def run_file_c(file: str, file_input: str) -> str:
    file_output = '{}/storage/{}'.format(str(Path.cwd()), str(uuid4()))
    command = 'gcc {} -o {} && {} < {}'.format(file, file_output, file_output, file_input)
    output = check_output(command, timeout=TIME_OUT, stderr=STDOUT, shell=True)
    output = output.strip()
    # remove file compile
    os.remove(file_output)
    return output.decode()


def run_file_cpp(file: str, file_input: str) -> str:
    file_output = '{}/storage/{}'.format(str(Path.cwd()), str(uuid4()))
    command = 'g++ {} -o {} && {} < {}'.format(file, file_output, file_output, file_input)
    output = check_output(command, timeout=TIME_OUT, stderr=STDOUT, shell=True)
    output = output.strip()
    # remove file compile
    os.remove(file_output)
    return output.decode()


def run_file_java(file: str, file_input: str) -> str:
    position = file.rfind('/')

    directory = file[:position]
    file_name = file[position+1:]
    file_build = file_name.replace('.java', '')

    command = 'cd {} && javac {} && java {} < {}'.format(directory, file_name, file_build, file_input)
    output = check_output(command, timeout=TIME_OUT, stderr=STDOUT, shell=True)
    output = output.strip()
    return output.decode()


def run_file_code(file: str, file_input: str) -> str:
    if file.endswith('.py'):
        return run_file_python(file, file_input)
    elif file.endswith('.c'):
        return run_file_c(file, file_input)
    elif file.endswith('.cpp'):
        return run_file_cpp(file, file_input)
    elif file.endswith('.java'):
        return run_file_java(file, file_input)
    else:
        raise RuntimeError("File code can't execute")
