import subprocess
def remove_file_in_storage(file_name):
    subprocess.run('rm '+file_name, shell=True)