# Part 3 - List/Tuple/Directory (extension)

#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
# Student ID - 20210218
# UOW Number - 19128544

#Creating veriables
progress = 0
trailer = 0
retriver = 0
excluded = 0

progressList = []
trailerList = []
retriverList = []
excludedList = []

def rangeChecker(inputCredit):
    if inputCredit in range(0,121,20):
        return True
    print("Out of range")

def progressionChecker(passCredits, deferCredits, failCredits):
    global progress, trailer, retriver, excluded

    if passCredits == 120:
        progressList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("Result - Progress")
        progress += 1
    elif passCredits == 100:
        trailerList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("Result - Progress (module trailer)")
        trailer += 1
    elif (passCredits == 40 and failCredits == 80) or (passCredits == 20 and (deferCredits <= 20)) or (passCredits == 0 and (failCredits >= 80)):
        excludedList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("Result - Exclude")
        excluded += 1
    else:
        retriverList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("Result - Module retriever")
        retriver += 1

def getUserInput():
    while True:
        try:
            while True:
                passCredits = int(input("Enter your total PASS credits: "))
                if rangeChecker(passCredits):
                    break

            while True:
                deferCredits = int(input("Enter your total DEFER credits: "))
                if rangeChecker(deferCredits):
                    break
                
            while True:
                failCredits = int(input("Enter your total FAIL credits: "))
                if rangeChecker(failCredits):
                    break
            
            if passCredits + deferCredits + failCredits != 120:
                print("Total incorrect")
                continue

            progressionChecker(passCredits, deferCredits, failCredits)
            break

        except ValueError:
            print("Integer required")
            passCredits = 0
            deferCredits = 0
            failCredits = 0
            continue


# Part 3 

def printAllValues():
    print()
    for i in progressList:
        print("Progress -", i)

    for i in trailerList:
        print("Progress (module trailer) -", i)
    
    for i in retriverList:
        print("Module retriever -", i)
    
    for i in excludedList:
        print("Exclude -", i)
    print()
    print()

# Result 

def resultsMenu():
    onceLoop = False
    while True:
           printAllValues()
           break

while True:
    getUserInput()
    while True:
        wantLoop = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if wantLoop == 'y' or wantLoop == 'q':
            break
    if wantLoop == 'q':
        resultsMenu()
        break
