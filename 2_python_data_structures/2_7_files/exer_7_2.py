"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""
# Use the file name mbox-short.txt as the file name
from pathlib import Path

fname = input("Enter file name: ")

current_file_path = Path(__file__).resolve()
root_dir = current_file_path.parents[2]
asset_file_dir = root_dir / "assets" / "files"
file_path = asset_file_dir / fname

total = 0
count = 0

if file_path.exists():
    try:
        fh = open(file_path)
        for line in fh:
            line = line.rstrip()
            if not line.startswith("X-DSPAM-Confidence:"):
                continue
            else:
                colon_pos = line.find(":")
                number_str = line[colon_pos + 1:].strip()
            
            try:
                number = float(number_str)
                count += 1
                total += number
            except Exception as e:
                print(e)
    except Exception as e:
        print(f"Something wrong while open file: {e}")
        quit()
else:
    print(f"File {fname} not found in directory {asset_file_dir}")
    quit()
    
avg_spam_confidence = total/count
print("Average spam confidence:", avg_spam_confidence)