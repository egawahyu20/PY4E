"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
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

list_of_words = []

for line in fh:
    words = line.split()
    for word in words:
        if word not in list_of_words:
            list_of_words.append(word)

list_of_words.sort()    
print(list_of_words)