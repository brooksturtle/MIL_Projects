import subprocess
import sys

# Joseph Brooks
# Checks NaviGator for all python files

# clearing text file
open("pythonPrograms.txt", "w").close()

# running git grep #!/usr/bin/env python and find .py
subprocess.call(['sh', 'bashPythonFinder'])

# reading each result from text file
file = open("pythonPrograms.txt", "r")
programLines = file.readlines()

# formatting text file and checking for duplicates
programList = []

counter = 0

for line in programLines:
    # get rid of git grep ending of program name
    if ":#!/usr/bin/env python" in line:
        line = line.replace(':#!/usr/bin/env python',"")
    # formatting issue cleaned up
    if line[0:2] == "./":
        line = line.replace('./', '')
    # do not add if duplicate
    if line in programList:
        pass
    else:
        counter = counter +1
        programList.append(line)
file.close()

# deleting this program from list 
del programList[-1]
counter = counter -1

file = open("pythonPrograms.txt", "w")

for program in programList:
    file.write(program)

print("Programs in pythonPrograms.txt")
print("{} Programs total".format(counter))
