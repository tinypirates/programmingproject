## task 3
"""AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"""

import csv, os, sys
from operator import itemgetter
    
def getcsv(): # does csv-y stuff
    reader_csv = csv.reader(file)

def sub_getcsv():
    global file
    with open(filereq+'.csv','r+') as file:
        getcsv()
    
def getclass_teacher(): # gets the file that the teacher wants to manipulate
    global filereq
    print("which class you wish to view results for?\n\n- class 1 [enter: class1]\n- class 2 [enter: class2]\n- class 3 [enter: class3]")
    filereq = input("please enter one of the options: ")
    if filereq == 'class1':
        sub_getcsv()
    elif filereq == 'class2':
        sub_getcsv()
    elif filereq == 'class3':
        sub_getcsv()
    else:
        print("\nsorry, a file was not found for that class")
        getclass_teacher()
getclass_teacher()

def getcsv_class():
    global csv_butts
    butts = open(filereq+'.csv')
    csv_butts = csv.reader(butts)


## ---------------------------- do stuff ---------------------------- ##

def alphabetically():
    print("\nthis is a list of students sorted in alphabetical order:")
    getcsv_class()
    alphabets = []
    for row in csv_butts:
        alphabets.append(row)
    for row in sorted(alphabets,key=lambda x:(str(x[0]),int(x[1]),int(x[2]))): #, reverse == False):
        print(row)
def highestscore02():
    butts = open('output.csv','r')
    csv_butts = csv.reader(butts)
    highest = []
    for row in csv_butts:
        highest.append(row)
    for row in csv_butts:
        print(row)
        
def highestscore():
    with  open("class1.csv","r") as r, open("output.csv","w", newline="") as file:
        csv_w = csv.writer(file)
        csv_r = csv.reader(r)
        csv_w.writerows(sorted((((name, max(scores,key=int))
                                 for name,*scores in csv_r)), key=itemgetter(1), reverse=False))
        file.close()
highestscore02()
     
    
def getoption():
    global optionreq
    print("\nhow do you wish to view the results for this class?\n\n- alphabetically by name [enter: 1]\n- average by score [enter: 2]\n- by highest by score [enter: 3]")
    optionreq = input("please enter one of the options: ")
    if optionreq == '1':
        alphabetically()
    elif optionreq == '2':
        highestscore() #pass
    elif optionreq == '3':
        pass
    else:
        print("\nnah m8")
getoption()
