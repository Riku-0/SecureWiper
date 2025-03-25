import os
import shutil
from secure_delete import secure_delete

def secure_delete_folder(folder_path, passes=5):
    """Securely delete all files and subdirectories in a folder."""
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return
    
    for root, _, files in os.walk(folder_path, topdown=False):
        for file_name in files:
            secure_delete(os.path.join(root, file_name), passes)
    
    shutil.rmtree(folder_path, ignore_errors=True)
    print(f"[OK] Securely deleted folder: {folder_path}")