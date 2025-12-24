import os
import shutil
import zipfile

def list_content(path='/content'):
    print(f"--- 📂 Mapping: {path} ---")
    for root, dirs, files in os.walk(path):
        # Prevent recursion into the agent's own git folder to keep logs clean
        if '.git' in dirs: dirs.remove('.git')
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{sub_indent}- {f}')

def zip_data(folder_to_zip, output_filename):
    print(f"🗜️ Zipping {folder_to_zip} into {output_filename}...")
    shutil.make_archive(output_filename.replace('.zip', ''), 'zip', folder_to_zip)
    print(f"✅ Archive created: {output_filename}")

def delete_target(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"🗑️ Deleted file: {path}")
        else:
            shutil.rmtree(path)
            print(f"🗑️ Deleted directory: {path}")
    else:
        print(f"⚠️ Path not found: {path}")

if __name__ == '__main__':
    # Default behavior: list the root
    list_content()