#----------------------------------------------------------------------------------
#Jeff Hejna
#11/17/14
#This program takes a directory file and allows the user to search the directory.
#
#                       Algorithm:
#                   1)obtain file
#                   2)allow user to search directory
#                   3)display the results of the search
#
#                       Algorithm for question 2:
#                   1)obtain file
#                   2)go through all entires in file
#                   3)display all repeats of same user entry
#
#-----------------------------------------------------------------------------------



def loadfile(filename):
    '''This function loads the files and obtains the information within it.'''
    data=[]
    f=open(filename,'r')
    for line in f:
        line=line.strip('\n')
        values = line.split(",")
        data.append(values)
    data.pop(0)
    f.close()
    return data

def dictionary(datalist):
    '''This function creates the dictionary.'''
    dictionary={}
    for line in datalist:
        dictionary[line[0]]=line[1]
    return dictionary    
        
    

def main():
    '''This is the main function that allows the user to search the directory.'''
    data=loadfile("Directory.csv")
    dict=dictionary(data)
    print("Welcome to out directory search!")
    print("You may enter a name to find a person's office, or enter an office to find the occupant.")
    n=0
    while n==0:
        info=input("Enter a name or location, or 'quit': ")

        for x in dict:
            if x==info:
                print(x,"can be found in: ",dict[x])
            elif dict[x]==info:
                print(dict[x],"is occupied by: ",x)
        if info=="quit":
            n+=1
            
        elif info not in list(dict.keys()) and info not in list(dict.values()):
            print(info,"not recognized as name or location,could you have meant any of the following?")
            for (x,y) in dict.items():
                if info in x:
                    print(x)
                elif info in y:
                    print(y)

        print()           

    
main()
