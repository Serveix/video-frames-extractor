import glob
import os
import uuid

path = './results'
i = 0

for filename in os.listdir(path):
    uuid_name = str(uuid.uuid4())
    os.rename(os.path.join(path,filename), os.path.join(path, uuid_name +'.jpg'))
    i += 1
