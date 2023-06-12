
import os
def gen_files_path(directory_path, target_directory):
    for dir_path, dir_names, file_names in os.walk(directory_path):
        if target_directory in dir_names:
            target_dir_path = os.path.join(dir_path, target_directory)
            for file in file_names:
                yield os.path.join(target_dir_path, file)
            if dir_path.endswith(target_directory):
                break


for file_path in gen_files_path('/', 'Users/ksenya'):
    print(file_path)

