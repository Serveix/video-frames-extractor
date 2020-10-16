import os
import argparse

parser = argparse.ArgumentParser("image_checker.py")
parser.add_argument("folder_path", help="Images folder path", type=str)
args = parser.parse_args()
path = args.folder_path

i = 0

for filename in os.listdir(path):
    filename_only = filename.split('.')[0]
    extension_only = filename.split('.')[1]

    if extension_only == 'jpg':
        if not os.path.isfile(os.path.join(path, filename_only + '.txt')):
            print(f"File {filename_only}.TXT missing!")
    elif extension_only == 'txt':
        if not os.path.isfile(os.path.join(path, filename_only + '.jpg')):
            print(f"File {filename_only}.JPG missing!")

    i += 1
