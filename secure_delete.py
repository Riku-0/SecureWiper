import os
import random
import time

def secure_delete(file_path, passes=5):
    """Securely delete a file by overwriting it multiple times and renaming it."""
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return
    
    file_size = os.path.getsize(file_path)

    with open(file_path, "wb") as file:
        for _ in range(passes):
            file.write(os.urandom(file_size))  # Random overwrite
            file.flush()
            os.fsync(file.fileno())
        file.write(b"\x00" * file_size)  # Final overwrite with zeros
        file.flush()
        os.fsync(file.fileno())

    # Rename file before deletion
    random_name = os.path.join(os.path.dirname(file_path), f"deleted_{random.randint(1000, 9999)}.tmp")
    os.rename(file_path, random_name)
    time.sleep(0.1)  

    os.remove(random_name)
    print(f"[OK] Securely deleted: {file_path}")