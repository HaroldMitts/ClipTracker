# This script will copy the contents of the clipboard to a text file and log file. It will also remove certain lines from the clipboard contents. 
# Author: Harold Mitts
# Date: February 15, 2023
# Version: 1.0.4
# Python Version: 3.9.1
# Dependencies: pyperclip, os, time, re, datetime
# Usage: Run the script and follow the prompts. The script will run until the user presses Ctrl+C. The script will also create a directory if it does not exist.
# More details can be found at https://github.com/HaroldMitts/ClipTracker 

import pyperclip
import os
import time
import re
from datetime import date

today = date.today()
date_string = today.strftime("%b-%d-%Y")

# Change this to the directory you want to save the text and log files to.
# If the directory does not exist, it will be created.
directory_path = "c:\\tmp"
if not os.path.exists(directory_path):
    os.mkdir(directory_path)
    print(f"Directory '{directory_path}' did not exist and has been created.")

filename = input("Enter filename (without extension): ")

text_file_path = f"{directory_path}\\{filename}.txt"
log_file_path = f"{directory_path}\\{filename}-log.txt"

if not os.path.exists(log_file_path):
    open(log_file_path, 'w', encoding='utf-8').close()
if not os.path.exists(text_file_path):
    open(text_file_path, 'w', encoding='utf-8').close()

# Add strings to this dictionary to remove them from the clipboard contents. Set the value to True to remove the line.
strings_to_delete = {
    ":": True,
    "HM": True,
    "LB": True,
    "SA": True,
    "ADDITIONAL_VALUES_TO_REMOVE_GO_HERE": True,
}

last_clipboard_contents = ""

try:
    while True:
        pyperclip.waitForNewPaste()
        current_clipboard_contents = pyperclip.paste()

        if current_clipboard_contents != last_clipboard_contents:
            last_clipboard_contents = ""
            lines = re.split(r'[\r\n]+', current_clipboard_contents)
            lines_to_keep = []
            deleted_lines = []
            for i, line in enumerate(lines):
                if line.startswith("Profile picture of ") or (len(line.strip()) == 2 and line.isupper()) or (line.strip() in strings_to_delete and strings_to_delete[line.strip()]):
                    deleted_lines.append(line.replace(":", ""))
                    if i < len(lines) - 1 and lines[i+1] == "":
                        deleted_lines.append(lines[i+1])
                        i += 1
                else:
                    lines_to_keep.append(line)
            lines_to_keep = [line.rstrip() for line in lines_to_keep if line.strip()]

            with open(text_file_path, 'a', encoding='utf-8') as f:
                f.write("\n".join(lines_to_keep) + "\n")
            with open(log_file_path, 'a', encoding='utf-8') as f:
                f.write("\n".join(deleted_lines) + "\n")
            if lines_to_keep:
                pyperclip.copy("\n".join(lines_to_keep))

        time.sleep(1)
        last_clipboard_contents = ""
except KeyboardInterrupt:
    print("Script stopped by user.")
    print("Text file path:", text_file_path)
    print("Log file path:", log_file_path)
    print("Exiting...")
    exit()
