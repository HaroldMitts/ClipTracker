# ClipTracker

This Python script monitors the clipboard for changes and logs deleted content to a file, while saving the remaining content to a text file. It is designed to help you keep track of your clipboard history and prevent unwanted content from being saved.

The script filters out unwanted content based on a predefined set of rules. By default, the script deletes lines that meet any of the following criteria:

The line is a colon character on a line by itself
The line begins with the string "Profile picture of"
The line consists of two uppercase letters only

These rules are defined in a dictionary called strings_to_delete, which can be modified to add or remove rules. To modify the rules, simply edit the strings_to_delete dictionary in the script to include or exclude specific strings and set the value to true. You can also set the value to false to prevent a string from being removed.

The script logs deleted content to a file called log.txt and saves the remaining content to a file called text.txt. Both files are saved in the c:\tmp directory by default, but the paths can be modified in the script if needed.

To use the script, simply run it in the background and copy any text to the clipboard as you normally would. The script will automatically filter out unwanted content and save the remaining content to the text.txt file.

Note that the script requires the pyperclip library to be installed, which can be installed using pip.

Run the script from the console then start copying text at-will. The script will continue to append the text.txt file with all your text copied. To exit, press Control-C in the console. Additional content can be written to the same text.txt file on subsequent runs, or you can backup/delete the text.txt file to start new.
