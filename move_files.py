import os
import shutil
from_dir="C:\Users\randh\Downloads"
to_dir="C:\Users\randh\OneDrive\Desktop\dowloded files"
list=os.listdir(from_dir)
print(list)
for file_name in list:
    name,extension=os.path.splitext(file_name)