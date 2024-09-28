import os
import shutil
import traceback

from name_manager import Name

def rename_files(root_dir, suffix_to_remove:str="watch"):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().startswith(suffix_to_remove):
                base_name, ext = os.path.splitext(filename)
                new_base_name = base_name[len(suffix_to_remove):].strip()
                new_filename = new_base_name + ext
                
                old_file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, new_filename)
                
                try:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed: {new_filename}")
                except Exception as e:
                    print(f"Error renaming {old_file_path}: {e}")

def move_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            target_path = os.path.join(root_dir, filename)
            name = Name(target_path, file_path)
            if name.is_series() or name.is_movie():
                path = name.get_path()
                print("Path:", path)
                os.makedirs(path, exist_ok=True)
                target_path = os.path.join(path, filename)
                
                print(file_path, target_path)
                try:
                    shutil.move(file_path, target_path)
                    print(f"Moved: {file_path} -> {target_path}\n")
                except Exception as e:
                    # print(f"Error moving {file_path} to movies: {e}")
                    traceback.print_exc()

rename_files(".")
move_files(".")


# name1 = Name("C:/Emmanuel/The leftover season 125 episode 7.mp4")
# name2 = Name("C:/Emmanuel/The leftover season 16 e 12.flv")
# name3 = Name("C:/Emmanuel/The leftover s 2 e 12.mkv")
# name3 = Name("C:/Emmanuel/Harry Potter.mkv")

# print(name1.get_series_name())
