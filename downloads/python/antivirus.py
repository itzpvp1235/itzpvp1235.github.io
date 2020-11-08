# This is my antivirus ting

import os

# Constants

VERSION = "BETA"
SUSPITIOUS_COMMENTS = ["virus", "bypass", "exploit", "riskware", "mallware", "ransomware"]
SENSITIVE_FILES = ["system32", "windows"]

# Functions


def progressBar(current, total):
    try:
        percent = (current / total) * 100
        percent = int(percent)

        final_string = "["

        for i in range(0, percent):
            final_string += "|"

        while not len(final_string) == 101:
            final_string+= " "

        final_string += "]"

        return final_string
    except ZeroDivisionError:
        return "[                                                                                                    ]"

# Code

try:
    while True:

        cmd = input("Enter command> ")
        cmd = cmd.split(" ")

        if cmd[0] == "scanfile":
            files = os.getcwd()
            files = os.listdir(files)
            files = [file.lower() for file in files]

            if cmd[1] not in files:
                print("Invalid file")
                print(f"Files in directory: {files}")

                continue

            else:
                cmd_ext = cmd[1]
                cmd_ext = cmd_ext.split(".")

                if cmd_ext[1] == "py":
                    print(f"Scanning {cmd_ext}")

                    os.system("cls")

                    print("Step 1: Pre-scan procedures")
                    print("Preparing to scan file...")

                    files_accessed = []
                    dangerous_signs = []
                    potentually_dangerous_signs = []
                    overall_threat_level = 0
                    progress = 0

                    print("\n")
                    print("Step 2: Checking file properties.")
                    print("Progress:")

                    with open(cmd[1], "r") as f:

                        lines = f.readlines()
                        print(f"length of file: {len(lines)}")
                        print("\n")
                        print("Step 3: Look for suspicious comments")

                        for count, line in enumerate(lines):
                            print(f"Progress: {progressBar(count+1, len(lines))}, Scanning line: {count}", end="\r")

                            splitLines = line.split("#")

                            if len(splitLines) == 2:
                                comment = splitLines[1]
                                comment = comment.strip()
                                word_comment = comment.split(" ")
                                SUSPITIOUS_COMMENTS = [i.lower() for i in SUSPITIOUS_COMMENTS]

                                for w in word_comment:
                                    for s in SUSPITIOUS_COMMENTS:
                                        w = w.lower()
                                        s = s.lower()

                                        if w == s:
                                            potentually_dangerous_signs.append(f"comment.{w}")

                        print("\n")

                        print("Step 4: Look for suspicious strings or sensitive files")

                        for count, line in enumerate(lines):
                            
                            print(f"Progress: {progressBar(count, len(lines)-1)}, Scanning line: {count}", end="\r")
                            
                            if '"' in line:
                                SENSITIVE_FILES = [temp.lower() for temp in SENSITIVE_FILES]

                                split_line = line.split('"')

                                toggle = False

                                for sl in split_line:
                                    if not toggle:
                                        toggle = True
                                    else:
                                        if sl.lower() == "del system32":
                                            dangerous_signs.append("This application is trying to delete system32")
                                        elif sl.lower() == "del windows":
                                            dangerous_signs.append("This application is trying to delete windows")
                                        elif sl.lower() == "del program files":
                                            dangerous_signs.append("This application is trying to delete the program "
                                                                   "files folder")

                                        elif sl.lower() == 'del "program files"':
                                            dangerous_signs.append("This application is trying to delete the program "
                                                                   "files folder")

                                        for sw in sl.split(" "):
                                            if sw.lower() in SENSITIVE_FILES:
                                                potentually_dangerous_signs.append(f"string.{sw}")

                                            if sw.lower() == "del":
                                                potentually_dangerous_signs.append(f"string.del")

                                        toggle = False

                        print("\n")

                        print("----------FILE SCAN RESULTS----------")

                        if len(dangerous_signs) > 0:
                            print("This file may be dangerous!")
                            print("\nDangerous signs")

                            for i in dangerous_signs:
                                print(i)

                            print("\n")

                        if len(potentually_dangerous_signs) > 0:
                            finished_string = ""

                            print("Potentually dangerous file contents:")
                            print("TYPE      CONTENTS")
                            for i in potentually_dangerous_signs:
                                i = i.split(".")

                                finished_string += i[0].ljust(10)
                                finished_string += i[1]
                                print(finished_string)

                                finished_string = ""

                        else:
                            print("This file is safe! No malicious code was detected.")

                        print("\n\n")



    #ERROR INFORMATION

                else:
                    print("File is not a python file")

        else:
            print("Unknown command")

    # EXIT FUNCTION

    exit()

except KeyboardInterrupt:
    print("Stopping PYAV")
    a = input("Are you sure you want to exit PYAV? Press enter to confirm")