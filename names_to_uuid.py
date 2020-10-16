import glob
import os
import uuid
import argparse

parser = argparse.ArgumentParser("names_to_uuid.py")
parser.add_argument("folder_path", help="Images folder path", type=str)
args = parser.parse_args()
path = args.folder_path

i = 0

for filename in os.listdir(path):

    uuid_name = str(uuid.uuid4())

    filename_only = filename.split('.')[0]
    extension_only = filename.split('.')[1]

    if extension_only == 'txt':
        print(f"Skipping extension: {extension_only}")
        continue

    print(f"Naming {filename_only}.jpg as {uuid_name}.jpg")
    os.rename(os.path.join(path, filename_only + '.jpg'), os.path.join(path, uuid_name + '.jpg'))

    print(f"Naming {filename_only}.txt as {uuid_name}.txt")
    os.rename(os.path.join(path, filename_only + '.txt'), os.path.join(path, uuid_name + '.txt'))
    print(" ")

    i += 1
