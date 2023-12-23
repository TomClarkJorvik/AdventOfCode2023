
possibleDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitDict = {"one":"1","two":"2","three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def parseWordRecursion(line, lineIndex, word, wordIndex):
    if (wordIndex < len(word)) and (lineIndex < len(line)):
        if line[lineIndex] == word[wordIndex]:
            if (wordIndex == (len(word)-1)):
                return True, word
            else:
                return parseWordRecursion(line, lineIndex+1, word, wordIndex+1)
    return False, ""

def parseWord(line, lineIndex):
    for digit in possibleDigits:
        if line[lineIndex] == digit[0]:
            isDigit, digit = parseWordRecursion(line, lineIndex+1, digit, 1)
            if isDigit:
                # Only return if it was a digit, otherwise keep searching
                return isDigit, digit
    return False, ""

def findListOfDigits(line):
    # Returns the list of digits in the order they appear.
    # Array is a list of strings.
    retArray = []            
    for i in range(len(line)):
        character = line[i]
        if character.isdigit():
            retArray.append(character)
        else:
            isDigit, digit = parseWord(line, i)
            if isDigit:
                retArray.append(digitDict[digit])
    return retArray

def findCalibrationFromLine(line):
    listOfDigits = findListOfDigits(line)
    
    firstDigit = listOfDigits[0]
    secondDigit = listOfDigits[len(listOfDigits)-1]

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