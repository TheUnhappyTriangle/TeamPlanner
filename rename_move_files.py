import os
import shutil

src_depth = 5
src_root = "C:\\Users\\Adam\\Downloads\\pokemon_sprites\\"
des_root = ".\\teamplanner\\src\\assets\\images\\sprites\\"

def list_files_at_depth(path, depth):
    if depth == 0:
        return
    
    path_array = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        #print(full_path)
        if os.path.isfile(full_path):
            path_array.append(full_path)
        elif os.path.isdir(full_path):
            subdir_files = list_files_at_depth(full_path, depth - 1)
            if subdir_files is not None:
                path_array.extend(subdir_files)
    #print(path_array)
    return path_array

def move_rename(src_files, des_root):
    #print("test")
    for filepath in src_files:
        #print(filepath)
        if filepath.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            #print("test")
            splitpath = os.path.normpath(filepath)
            splitpath = splitpath.split(os.sep)
            gennum = splitpath[5].split("-",1)[1]
            gamenames = splitpath[8].split("-")
            gameabbrev = ''.join([name[0] for name in gamenames])
            dexnum = os.path.splitext(os.path.basename(filepath))[0]
            file_ext = ".png"
            if filepath.lower().endswith(('.gif')):
                file_ext = ".gif"
            newfilename = gennum+"_"+gameabbrev+"_"+"reg"+file_ext
            destination_path = os.path.join(des_root+dexnum+"\\", newfilename)

            try:
                shutil.copy2(filepath, destination_path)
                print(f"Moved and renamed: {filepath} -> {destination_path}")
            except Exception:
                print(destination_path+" Does not exist")
            

src_paths = list_files_at_depth(src_root, src_depth)

move_rename(src_paths, des_root)