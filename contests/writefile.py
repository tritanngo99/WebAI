from pathlib import Path
path = Path(__file__)
root_path = str(path.parent.parent)+'/storage/'

def handle_upload_file(file):

    with open(root_path + str(file),'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
def write_input(text):
    f = open('./storage/inp.txt', 'w+')
    f.write(text)