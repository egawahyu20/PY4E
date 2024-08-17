"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
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

hour_dictionary = dict()

for line in fh:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time[:2]
        hour_dictionary[hour] = hour_dictionary.get(hour, 0) + 1

for x, y in sorted(hour_dictionary.items()):
    print(x, y)