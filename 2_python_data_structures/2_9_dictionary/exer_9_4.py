"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
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

email_dictionary = dict()

for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_dictionary[email] = email_dictionary.get(email, 0) + 1
        
max_count = None
max_email = None

for email, count in email_dictionary.items():
    if max_count is None or count > max_count:
        max_count = count
        max_email = email

print(max_email, max_count)