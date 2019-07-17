#------------------------------------------------------------------------------------
# Jeff Hejna
# 11/11/14
# This program takes a calendar text file and allows the user to edit/display/save
# their calendar.
#
#                       Algorithm
#           1)Obtain the calendar text file
#           2)Allow the user to be able to display/add/save to the calendar.
#           3)Allow the user to quit out of the program when they are done.
#
#------------------------------------------------------------------------------------



def openfile(file):
    '''This funtion opens up the file.'''
    data=[]
    f=open(file,'r')
    for line in f:
        line=line.strip('\n') #gets rid of \n from lines
        values=line.split()
        data.append(values)    
    f.close()
    return data

def choiceD(alist):
    '''This funtion displays the calendar in a nice format.'''
    for x in alist:
        Year=x[0]
        Month=x[1]
        Date=x[2]   #gets appropriate values for what is in alist
        Time=x[3]   #and prints them out in a chart
        Text=x[4:]
        Text=' '.join(Text)
        print("%s \t %s \t %s \t %s \t %s" % (Year,Month,Date,Time,Text))


def choiceA(mainlist):
    '''This function lets the user add a new event to the calendar.'''
    
    year=(input("Enter the year of the event: "))
    month=(input("Enter the month(01-12) of the event: "))
    day=(input("Enter the day(01-31) of the event: "))
    time=(input("Enter the time of the event (0000-2400): "))
    text=input("Enter what the event is: ")

    newlist=[] #new list of the new event
    newlist.append(year)
    newlist.append(month)
    newlist.append(day)
    newlist.append(time)
    newlist.append(text)
    
    mainlist.append(newlist) #adds the new element to list
    titleList=mainlist[0] #the title(Year,Month,Date,Time,Text)
    altList=mainlist[1:] #gets rid of the title

    altList.sort() #sorts the lists
    altList.insert(0,titleList) #inserts the title back after it has been sorted 
    return altList

def choiceS(datalist):
    '''This funtion saves the current calendar to the calendar.txt file.'''
    file=open("calendar.txt",'w')
    string=""
    for list in datalist:
        string=' '.join(list)#turns each list into a string
        file.write(string+'\n')#wrties new string into the file
    file.close()    
            

def main():
    '''This is the main function that will call the various functions depending on what the user inputs.'''
    n=0
    datalistPRIME=openfile("calendar.txt")#original calendar
    datalist=openfile("calendar.txt")#potentially edited calendar
    while n==0:
        choice=input("Would you like to [d]isplay the calendar, [a]dd to the calendar, [s]ave current calendar, or [q]uit ? ")
        if choice=='d'or choice=='D':
            print()
            print("Here is what your current calendar looks like: ")
            print()
            choiceD(datalist)
            print()
        
        elif choice=='a'or choice=='A':
            print()
            print("Okay, let's add an event to the calendar!")
            print()
            datalist=choiceA(datalist)
            print()
            print("Okay, this is your updated calendar: ")
            print()
            choiceD(datalist)
            print()
    
        elif choice=='s'or choice=='S':
            print()
            choiceS(datalist)
            print("Your calendar has been saved!")
            print()
        
        elif choice=='q' or choice=='Q':
            print()
            print("This is what your ORIGINAL calendar looked like: ")
            print()
            choiceD(datalistPRIME)
            print()
            print("This is what your UPDATED calendar looks like: ")
            print()
            choiceD(datalist)
            print()

            pick=input("Do you want to save your current calendar before you quit? (y/n): ")
            if pick=='y' or pick=='Y':
                choiceS(datalist)
                print("Okay, any updates to the calendar were saved! Goodbye!")
            elif pick=='n' or pick=='N':
                print("Okay, any updates to the calendar were not saved if you didn't save beforehand. Goodbye!")
            
            n+=1 #this will cause the program to terminate
        else:
            print()
            print("ERROR!!: You typed in something that wasn't [d],[a],[s],or [q]. Please choose the appropriate option next time.")
            print()
    
                  
                  
                  
            
        

main()                    
                    
