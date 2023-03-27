# Part 4 - Text File

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
        print("Result - Progress (module trailer")
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
                print()
                if rangeChecker(passCredits):
                    break

            while True:
                deferCredits = int(input("Enter your total DEFER credits: "))
                print()
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
def saveData():
    txtFile = open("Assessment Text File.txt", "w")

    for i in progressList:
        txtFile.writelines("Progress - " + i + "\n")

    for i in trailerList:
        txtFile.writelines("Progress (module trailer) - " + i + "\n")
    
    for i in retriverList:
        txtFile.writelines("Module retriever - " + i + "\n")
    
    for i in excludedList:
        txtFile.writelines("Exclude - " + i + "\n")

    txtFile.close()
    print()

def loadData():
    txtFile = open("Assessment Text File.txt", "r") 
    print("----------------DATA FROM .TXT FILE-----------------")
    print(txtFile.read())
    print()
    txtFile.close()
 

def resultsMenu():
    onceLoop = False
    while True:
            
            saveData()
            loadData()
            break
        
#getting input to quit or to enter another  set of data
               
while True:
    getUserInput()
    while True:
        print("Would you like to enter another set of data?")
        print()
        wantLoop = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print()
        if wantLoop == 'y' or wantLoop == 'q':
            break
    if wantLoop == 'q':
        resultsMenu()
        break

