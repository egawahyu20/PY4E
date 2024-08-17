"""
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""
# Use words.txt as the file name
from pathlib import Path

fname = input("Enter file name: ")

current_file_path = Path(__file__).resolve()
root_dir = current_file_path.parents[2]
asset_file_dir = root_dir / "assets" / "files"
file_path = asset_file_dir / fname

if file_path.exists():
    try:
        fh = open(file_path)
    except Exception as e:
        print(f"Something wrong while open file: {e}")
        quit()
else:
    print(f"File '{fname}' not found in directory '{asset_file_dir}'.")
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())