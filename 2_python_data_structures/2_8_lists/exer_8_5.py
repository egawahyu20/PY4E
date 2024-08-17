"""
Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). 
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

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
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")