import os
import shutil
import sys
import argparse

# Function to list all files and directories
def list_files(path, show_hidden=False):
    try:
        # List all files in the directory
        entries = os.listdir(path)
        if not show_hidden:
            entries = [entry for entry in entries if not entry.startswith('.')]
        return entries
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

# Function to create a new directory
def create_directory(path, dir_name):
    try:
        dir_path = os.path.join(path, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            print(f"Directory '{dir_name}' created at {path}")
        else:
            print(f"Directory '{dir_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Function to delete a directory
def delete_directory(path, dir_name):
    try:
        dir_path = os.path.join(path, dir_name)
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"Directory '{dir_name}' deleted.")
        else:
            print(f"Directory '{dir_name}' does not exist.")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# Function to move a file or directory
def move_item(src_path, dest_path):
    try:
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)
            print(f"Moved {src_path} to {dest_path}")
        else:
            print(f"{src_path} does not exist.")
    except Exception as e:
        print(f"Error moving item: {e}")

# Function to rename a file or directory
def rename_item(path, old_name, new_name):
    try:
        old_path = os.path.join(path, old_name)
        new_path = os.path.join(path, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
        else:
            print(f"{old_name} does not exist.")
    except Exception as e:
        print(f"Error renaming item: {e}")

# Main function for the CLI file manager
def file_manager():
    parser = argparse.ArgumentParser(description="A simple CLI file manager")
    
    # Adding arguments
    parser.add_argument("path", help="Path to the directory to manage")
    parser.add_argument("-l", "--list", action="store_true", help="List files in the directory")
    parser.add_argument("-c", "--create", type=str, help="Create a new directory with this name")
    parser.add_argument("-d", "--delete", type=str, help="Delete a directory with this name")
    parser.add_argument("-m", "--move", type=str, nargs=2, help="Move an item from source to destination")
    parser.add_argument("-r", "--rename", type=str, nargs=2, help="Rename an item from old name to new name")
    parser.add_argument("-H", "--hidden", action="store_true", help="Show hidden files")
    
    args = parser.parse_args()

    # Ensure the path exists
    if not os.path.exists(args.path):
        print(f"The path {args.path} does not exist.")
        sys.exit(1)

    if args.list:
        # List the files and directories
        files = list_files(args.path, args.hidden)
        if files:
            print("Files and directories in", args.path)
            for file in files:
                print(file)

    if args.create:
        # Create a new directory
        create_directory(args.path, args.create)

    if args.delete:
        # Delete a directory
        delete_directory(args.path, args.delete)

    if args.move:
        # Move a file or directory
        src, dest = args.move
        move_item(os.path.join(args.path, src), os.path.join(args.path, dest))

    if args.rename:
        # Rename a file or directory
        old_name, new_name = args.rename
        rename_item(args.path, old_name, new_name)

if __name__ == "__main__":
    file_manager()
