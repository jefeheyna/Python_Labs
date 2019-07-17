#----------------------------------------------------------------------------
#Jeff Hejna
#11/4/14
#Lab 9
#
#The purpose of this program is to provide the stats about quiz grades from a file.
#
#                   Algorithm:
#       1)Obtain file of information
#       2)Find the max,min,mean,median,and mode of the values for each person
#       3)Organize information into a chart
#
#-----------------------------------------------------------------------------


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
        


def numlist(alist):
    '''This function gets the lists of numbers from the file list.'''
    numlist=[]
    
    for item in range(len(alist)):
        nonames=alist[item][1:len(alist)] #cuts out the names from list
        numlist.append(nonames)
    finalnumlist=[]
        
    for x in numlist:
        ints=list(map(int,x)) #turns str numbers to ints
        finalnumlist.append(ints)    

    return finalnumlist

def namelist(alist):
    '''This funtion gets the names from the file list.'''
    namelist=[]
    for item in range(len(alist)):
        names=alist[item][0] #leaves just names in list
        namelist.append(names)
    print(namelist)    
    return namelist    
        

def max_list(numlist):
    '''This function gets the max values from the lists.'''
    maxlist=[]
    largest=0
    for item in numlist:
        for num in item:
            if num>=largest:
                largest=num
        maxlist.append(largest)
        largest=0
    return maxlist

def min_list(numlist):
    '''This function gets the min values from the lists.'''
    minlist=[]
    smallest=10
    for item in numlist:
        for num in item:
            if num<smallest:
                smallest=num
        minlist.append(smallest)
        smallest=10
    return minlist
                
def mean_list(numlist):
    '''This function gets the mean values from the lists.'''
    totallist=[]
    total=0
    for item in numlist:
        for num in item:
            total+=num #creates list of totals for each list
        totallist.append(total)
        total=0
    meanlist=[]
    for x in totallist:
        meanlist.append(x/len(item)) #creates list of mean numbers
    return meanlist

def median_list(numlist):
    '''This function gets the median values from the lists.'''
    medianlist=[]
    for alist in numlist:
        alist.sort()
        median=""
        while median=="":
            length=len(alist)
            if length>2:
                del(alist[0]) #removes first and last numbers from list
                del(alist[len(alist)-1]) #until only 2 remain
            elif length==2:
                median=alist[1] #picks the median number
            else:
                median=alist[0]
        medianlist.append(median)        
       
    return medianlist

def mode_list(numlist):
    '''This function gets the mode values from the lists.'''
    modelist = []
    for item in numlist:
        item.sort()
        maxlist = []
        for value in item:
            if value not in maxlist:
                maxlist.append(value) #creates new list without duplicates
        maxcount = 0
        for value in maxlist:
            count = 0
            for num in item:
                if value == num:
                    count += 1
            if count > maxcount:
                maxcount = count
                mode = value
        modelist.append(mode)
    return(modelist)

def printNums(names, maxNums, minNums, means, medians, modes):
    '''This function formats the results into a nice chart.'''
    print ("Name \t\t |Max \t |Min \t |Mean \t |Median  |Mode" %())
    print ('---------------------------------------------------------')
    for x in range(len(names)):
        name = names[x]
        maxNum = maxNums[x]
        minNum = minNums[x]
        mean = means[x]
        median = medians[x]
        mode = modes[x]
        print ("%s \t |%d \t |%d \t |%d \t |%d \t  |%d \n" % #roomate taught me this
               (name, maxNum, minNum, mean, median, mode))


def main():
    '''This is the main function that takes in all the other values and prints out the results.'''
    datalist=loadfile("Lab9file.csv")
    numbers=numlist(datalist)
    names=namelist(datalist)
    max_nums=max_list(numbers)
    min_nums=min_list(numbers)
    mean_nums=mean_list(numbers)
    mode_nums=mode_list(numbers)
    median_nums=median_list(numbers)
    printNums(names, max_nums, min_nums, mean_nums, median_nums, mode_nums)

main()
    
