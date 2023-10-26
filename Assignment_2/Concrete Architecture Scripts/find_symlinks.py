import os

for foldername, subfolders, filenames in os.walk("./"):
    for filename in filenames:
        filepath = os.path.join(foldername, filename)
        if os.path.islink(filepath):
            print(f"Symlink found: {filepath}")
            
    for subfolder in subfolders:
        subfolderpath = os.path.join(foldername, subfolder)
        if os.path.islink(subfolderpath):
            print(f"Symlink found: {subfolderpath}")
