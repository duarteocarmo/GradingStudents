#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:03:31 2017

@author: duarteocarmo
"""
#import relevant libraries and functions.
import matplotlib.pyplot as plt
import numpy as np
from GradingStudents_computeFinalGrades import computeFinalGrades
from GradingStudents_roundGrade import roundGrade
import pandas as pd



#This function takes a grades matrix and plots all of the grades.
def gradesPlot(grades):

#-------------------BAR PLOT----------------------------------------

#Get the final grades using the computeFinalGrades function
#Create a vector of possible grades
#Create a vector of frequencies the size of the possible grades
    finalgrades=computeFinalGrades(grades)
    finalgrades=finalgrades.reshape(1,-1)
    possiblegrades=np.array([[-3, 0, 2, 4, 7, 10, 12]])             
    frequency=np.zeros(np.size(possiblegrades))
    
#this function iterates simultaniously through the possible grades 
#to get the frequency of every grade
    for (i,j) in zip(range(0,7), np.nditer(possiblegrades)):        
            frequency[i]=finalgrades[finalgrades==j].size         

#This line removes the uni dimensional elements and transforms into an array            
    possiblegrades = np.squeeze(np.asarray(possiblegrades))        
    
#These lines plot the bar plot, determining the width, x intervals, 
#titles, and grids.    
    width = 1/1.5                                                 
    plt.bar(possiblegrades,frequency, width, color="blue")
    plt.xticks(possiblegrades)
    plt.title("Final Grades")
    plt.xlabel("Possible Grades")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()
    
#-------------------ASSINGNEMENTS PLOT----------------------------------------    

#Get the number of assignments, the number of students(classsize) and 
#create a vector 'm' with all of the numbersof the assignments, a range from 1 
#to the number of assignments+1 for readability.     
    assignmentnumber=grades.shape[1]                            
    classsize=grades.shape[0]                                       
    m=np.arange(1,assignmentnumber+1)                             

#This loop runs through all of the students and creates a student vector that
#is a vector with all of his grades. After that, if he has a "weird" grade 
#it skips the plot and print a warning, if not, the plot is made. 
    for i in range(classsize):
        student=grades[i,:]
        if np.amax(student)>12 or np.amin(student)<-3:
            print('WARNING! A student with invalid grades was plotted. Please check menu option 2 for more details.')
            plt.plot(m,student,"b8",label='_nolegend_')
            m=m+0.04
            continue
        else:                                         
            plt.plot(m,student,"b8",label='_nolegend_')
            
#m adds a small space between each plot by adding 0.04 to the x axis. 
            m=m+0.04 
        
#These two lines, calculate the raw mean of the grades and then attributes
#that raw mean to a particular grade using the roundgrade function. 
#So that the mean wont be something like 5.6 and it is 7 instead.
    rawmeans=grades.mean(0)
    finalmeans=roundGrade(rawmeans)                                
    
#Plot the function   
    plt.plot(np.arange(1,assignmentnumber+1),finalmeans,"r-",label="Means")
    plt.xticks(np.arange(1,assignmentnumber+1))
    plt.yticks(possiblegrades)
    plt.title("Grades per assignment")
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.grid()    
#Put legend outside of the plot.     
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
    plt.show()
                   

    
    
    
    
 
    
    
    

    

