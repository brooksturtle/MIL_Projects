import os
import re

# Joseph Brooks
# Checks NaviGator for all python files
print("Python Finder")
print("Type directory path you want to search from")
directory = input(": ")

# clearing text file
open("pythonPrograms.txt", "w").close()
allFileList = []


# gets all files in directory
for root, dirs, files in os.walk(directory):
    for name in files:
        programName = os.path.join(root, name)
        allFileList.append(programName)


pythonList = []

# attempts to open file as text and checks #!/usr/bin/env
for program in allFileList:
    try:
        for line in open(program):
            if re.search("#!/usr/bin/env", line):
                pythonList.append(program)
            break
    except:
        pass

# checks for ending .py
for program in allFileList:
    if '.py' in program:
        pythonList.append(program)

# checking for duplicates
finalList = []

for program in pythonList:
    # do not add if duplicate
    if program in finalList:
        pass
    else:
        finalList.append(program)

file = open("pythonPrograms.txt", "w")

counter = 0
# writing to file
for program in finalList:
    file.write(program + "\n")
    counter = counter + 1
file.close()

print("{} Programs total".format(counter))
print("Programs in pythonPrograms.txt")
