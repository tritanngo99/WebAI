from pathlib import Path
def handle_upload_file(file):
    path = Path(__file__)
    root_path = str(path.parent.parent)+'/storage/'
    # with open(root_path + str(file),'wb+') as destination:
    #     for chunk is file.chunks():
    #         destination.write(chunk)
    print(root_path)
if __name__ == '__main__':
    handle_upload_file('name')