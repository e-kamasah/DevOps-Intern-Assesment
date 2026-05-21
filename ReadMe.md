# Task 1: Automation Script
# Directory monitoring Script

## Overview
The Python script(monitor.py) scans a directory that has been specified i.e in my case a local directory on my desktop(C:\Users\kamas\OneDrive\Desktop\Test) once and provides information on the contents inside the directory. This includes:
-Filename
-File size(KB)
-Timestamp of the scan.
The results of the scan is then saved in the log.txt file.

The log file is saved in the same directory unless you specify a custom path you want it to save to.
On each run, the script only checks the directory once and exits thus does not run in the background. 

## How to run the script
1. Ensure that you have Python installed on your machine.
2. Clone the repo to your device and open in vs code or any other supported IDE
3. Update the directory path inside the script:
    ```python
   directory_to_monitor = r"C:\Users\kamas\OneDrive\Desktop\Test" to your custom directory.
4. Run the script monitor.py
5. The log.txt will be generated and will contain the result of the script when sucessfull 

# NB
In Python, \U starts an escape sequence (like \n for newline, \t for tab). So \Users gets misinterpreted as “start of a Unicode escape” so we prefix the string with r so backslashes are treated literally. So remember to check and have a correct file path depending on which os you are using.
