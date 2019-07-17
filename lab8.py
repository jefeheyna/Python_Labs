#--------------------------------------------------------------------------------------------------------------------------
# Jeff Hejna
# 10/27/14
# Lab 8
#
# This program will take a string and find the number of words, the average length of the words, and the proper nouns.
#
#                      Algorithm
#                1) Create a string
#                2) Get the number of words, average length of the words, and proper nouns.
#                3) Print the results
#
#----------------------------------------------------------------------------------------------------------------------------

def getAllLetters(astring):
    '''This function takes a string and turns that string into a list and returns that list to main().'''
    stringList=astring.split()  #turns string into list
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    newList = []    #newList that doesn't have anything but letters and '' "
    for words in stringList:
        lettersInWords = list(words[:])
        newString = ''
        for x in lettersInWords: #creates newList with just letters
            y = x in letters
            if y == True:
                newString += x
        newList.append(newString)
    finalList=[]    
    for x in newList:   # gets rid of '' in newList and creates finalList
        if x!='':
            finalList.append(x)
            
    print(finalList)        
    return finalList #returns finalList to the variable allLetters in main()

def getNumOfWords(newStringList):
    '''This function counts the number of words in the list.'''
    count = len(newStringList)
    return (count)

def getAvgLength(newStringList):
    '''This function gets the average length of the words in the list.'''
    NumWords=len(newStringList)
    LengthOfWords=[]
    for x in newStringList:
        length=len(x)
        LengthOfWords.append(length)
    avgLength=sum(LengthOfWords)/NumWords
    return avgLength
        

def getPropNouns(newStringList):
    '''This function finds all the proper nouns in the list.'''
    CapLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PropNounList=[]
    for x in newStringList: #gets the proper nouns
        if x[0] in CapLetters:
            PropNounList.append(x)
    return PropNounList        
            
    
def printStats(wordCount, avgLen, propNouns):
    '''This function prints the word count, average length of the words, and the proper nouns.'''
    print("The number of words is: ",wordCount)
    print("The average length of the words is: ",avgLen)
    print("The proper nouns are: ",propNouns)

    
def main():
    '''This function stores all the returned values from the other functions into variables that are then sent to the printStats() function.'''
    string = input("Input something you would like the stats of: ")
    allLetters = getAllLetters(string)
    wordCount = getNumOfWords(allLetters)
    avgLen = getAvgLength(allLetters)
    propNouns = getPropNouns(allLetters)
    printStats(wordCount, avgLen, propNouns)
    
main()
    
    
