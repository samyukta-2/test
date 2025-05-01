import os

folder_path = r'C:\path\to\your\folder'  
base_name = "renamed_file"

files = os.listdir(folder_path)
for index, filename in enumerate(files):
    file_ext = os.path.splitext(filename)[1]  
    new_name = f"{base_name}_{index+1}{file_ext}"

    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    os.rename(src, dst)
    print(f"Renamed: {filename} → {new_name}")
