
def findCalibrationFromLine(line):
    firstDigit = ""
    secondDigit = ""
    for character in line:
        if character.isdigit():
            if firstDigit == "":
                firstDigit = character
                secondDigit = character
            else:
                secondDigit = character

    retVal = int(firstDigit + secondDigit)
    return retVal

runningCalibrationVal = 0
file = open("input.txt")
for line in file:
    line = line.strip()
    lineCalibrationVal = findCalibrationFromLine(line)
    runningCalibrationVal += lineCalibrationVal
file.close()
print(runningCalibrationVal)