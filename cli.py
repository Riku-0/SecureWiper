import sys
import os
from secure_delete import secure_delete
from secure_folder import secure_delete_folder

def run_cli():
    """Command-line interface for secure file deletion."""
    if len(sys.argv) < 2:
        print("Usage: python main.py cli <file/folder> [passes]")
        return

    items = sys.argv[2:]
    passes = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 5

    for item in items:
        item = os.path.abspath(item)  # Get absolute path
        if os.path.isfile(item):
            secure_delete(item, passes)
        elif os.path.isdir(item):
            secure_delete_folder(item, passes)
        else:
            print(f"[ERROR] Not found: {item}")

if __name__ == "__main__":
    run_cli()