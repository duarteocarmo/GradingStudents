#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:34:45 2017

@author: duarteocarmo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:06:12 2017

@author: duarteocarmo
"""
#import relevant libraries
import numpy as np
import pandas as pd
import glob

#import relevant functions from other files. 
from GradingStudents_computeFinalGrades import computeFinalGrades
from GradingStudents_gradesPlot import gradesPlot
from GradingStudents_roundGrade import roundGrade
from GradingStudents_displayMenuFinal import displayMenu

print("Welcome to Program for grading students!")

#-----------------------LOAD FILE FIRST----------------------------------------
while True:
    try:       
        print("Files eligible to load:")  
#This command "glob.glob(x)" looks through all files in the 
#working directory. By using print(glob.glob('*.csv')), only files with the .csv will appear

        print(glob.glob('*.csv'))
        
#Ask for filename to user and presents it to the user.                 
        filename=input("Please enter the name of your data file ensuring that you type .csv afterwards: ")
        raw_data= pd.read_csv(filename)
        matrix=np.array(raw_data.iloc[:,:])
        print("We found your file!")
        print(matrix)
        print("You have evaluated a total of {} students in {} assignments.".format(matrix.shape[0],matrix.shape[1]-2))  

# If error happens, try again.                                                                       
    except IOError:               
        print("Sorry, we could not find your file,please try again...")                                         
    else:
        break  

#create all menu options in a menuItems array
menuItems = np.array(["Load new data.", "Check for data errors.", "Generate plots.", "Display list of grades. ", "Quit."])

#-----------------------LAUNCH MENU AFTER FILE LOADED--------------------------

while True:
    choice = displayMenu(menuItems)

    #-----------------------NEW LOAD-------------------------------------------   
    if choice == 1:
        while True:
            try:
#repeat loading file process described above. 
                print("Files eligible to load:")
                print(glob.glob('*.csv'))                
                filename=input("Please enter the name of your data file ensuring that you type .csv afterwards: ")
                raw_data= pd.read_csv(filename)
                matrix=np.array(raw_data.iloc[:,:])
                print("We found your file!")
                print(matrix)
                print("You have evaluated a total of {} students in {} assignments.".format(matrix.shape[0],matrix.shape[1]-2))                                                                         #run dataload function with file requested
            except IOError:
                print("Sorry, we could not find your file,please try again...")                                         
            else:
                break
    #-----------------------CHECK FOR ERRORS-----------------------------------
    if choice== 2:
        
#checks for duplicated student id's
        studentlist=matrix[:,0]
        unique=np.unique(studentlist)
        occurrence=np.zeros(np.size(unique))
        for i in range(np.size(unique)):
            for j in range (np.size(studentlist)):
                if unique[i]==studentlist[j]:
                    occurrence[i]=occurrence[i]+1
                else:
                    pass
#if occurrence over 1 display error:
#this does NOT erase the error. Since the assignment did not request this feature.
        if np.size(unique[occurrence>1])>0:
            print("The following student ID(s) are repeated: {} .".format(unique[occurrence>1])) 
        else:
            print("No repetitions were found.")

#checks for grades that are bad    
        grades=matrix[:,2:]
        possiblegrades=np.array([[-3, 0, 2, 4, 7, 10, 12]])
        ri=0
        for i in range(grades.shape[0]):
            for j in range(grades.shape[1]):
#if grade not in the possible grades vector, display error. 
#this does NOT erase the error. Since the assignment did not request this feature.
                if grades[i,j] not in possiblegrades:
                    print("Bad grade found with value '{}' given to {}, should be in line {}.".format(grades[i,j],matrix[i,1],i+1))
                    ri=ri+1
                else:
                    pass
        if ri==0:
            print("No weird grades. Hurray!")
            
    #-----------------------PLOT-----------------------------------------------
#plots the user's file           
    if choice == 3:
        gradesPlot(matrix[:,2:])

    #-----------------------PRESENT LIST OF GRADES-----------------------------   
    if choice == 4:
       
#by transposing, present the grades for each assignment.
        grades=matrix[:,2:]
        byassignment=grades.T
        print('Here are the grades for each assignment you corrected:')
        for i in range(byassignment.shape[0]):
            print("Assignment number {} has the following grades:{}.".format(i+1, byassignment[i,:]))
        
#compute vector of finalgrades and vector of finalnames
#horizontally stacks them and sorts them in alphabetical order.        
        finalgrades=computeFinalGrades(grades)
        finalnames= np.reshape(matrix[:,1], [-1, 1])
        Studentlist=np.hstack((finalnames,finalgrades))
        final=sorted(Studentlist,key=lambda x:x[0])
        final=np.reshape(final,[-1,2])
        print("Here are the final grades for each student:")
        print(final)

        
    #-----------------------QUIT----------------------------------------------  
#quit if choice =5 and display goodby message         
    if choice == 5:
        print("It was nice having you.Goodbye.")
        break
        


  
    