import os

dir_path = "C:\\Users\\Adam\\Downloads\\pokemon_sprites"

def list_files_at_depth(path, depth):
    if depth == 0:
        return

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            split_path = os.path.normpath(full_path)
            split_path = split_path.split(os.sep)
            print(split_path)
            print(os.path.splitext(os.path.basename(full_path)))
            print(split_path[5].split("-",1)[1])
            print(split_path[8])
        elif os.path.isdir(full_path):
            list_files_at_depth(full_path, depth - 1)

# Set the desired depth of subfolders to list the files (e.g., depth 1, depth 2, etc.)
depth = 5

# Call the function to list files at the specified depth of subfolders
list_files_at_depth(dir_path, depth)

# python .\list_dirs.py