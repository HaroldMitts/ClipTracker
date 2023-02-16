import pyperclip
import os
import time
import re
from datetime import date

today = date.today()
date_string = today.strftime("%b-%d-%Y")

text_file_path = "c:\\tmp\\text.txt"
log_file_path = "c:\\tmp\\log.txt"

new_text_filename = input("Enter new text filename (without extension): ")
new_log_filename = input("Enter new log filename (without extension): ")

if new_text_filename:
    text_file_path = f"c:\\tmp\\{new_text_filename}-{date_string}.txt"
if new_log_filename:
    log_file_path = f"c:\\tmp\\{new_log_filename}-log-{date_string}.txt"

if not os.path.exists(log_file_path):
    open(log_file_path, 'w', encoding='utf-8').close()
if not os.path.exists(text_file_path):
    open(text_file_path, 'w', encoding='utf-8').close()

strings_to_delete = {
    ":": True,
    "Raj G": True,
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