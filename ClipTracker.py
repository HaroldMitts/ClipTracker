import pyperclip
import os
import time

log_file_path = "c:\\tmp\\log.txt"
text_file_path = "c:\\tmp\\text.txt"

if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()
if not os.path.exists(text_file_path):
    open(text_file_path, 'w').close()

strings_to_delete = {
    ":": True,
    "Raja Gonna Getcha": True,
    "HM": True,
    "REMOVE": True
}

last_clipboard_contents = ""

while True:
    pyperclip.waitForNewPaste()
    current_clipboard_contents = pyperclip.paste()

    if current_clipboard_contents != last_clipboard_contents:
        last_clipboard_contents = ""
        lines = current_clipboard_contents.split("\n")
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
        with open(text_file_path, 'a') as f:
            f.write("\n".join(lines_to_keep) + "\n")
        with open(log_file_path, 'a') as f:
            f.write("\n".join(deleted_lines) + "\n")
        if lines_to_keep:
            pyperclip.copy("\n".join(lines_to_keep))

    time.sleep(1)
    last_clipboard_contents = "" # Reset the variable at the end of the loop
