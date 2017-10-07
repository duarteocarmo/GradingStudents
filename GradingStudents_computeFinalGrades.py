#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:16:37 2017

@author: duarteocarmo
"""


#import relevant libraries
import numpy as np
from GradingStudents_roundGrade import roundGrade


#This function receives as input a list of grades and computes the final grade for
#each student

def computeFinalGrades(grades):
    
#Define the number of students, the number of assignments and create a 
#final grade matrix. Also create a matrix of 0's the size of the inicial matrix.
    
    gradesFinal=np.array    
    students=grades.shape[0]            
    assignments=grades.shape[1]        
    allzeros=np.zeros(grades.shape) 
    
#if only one assingment is detected, the final grades is equal to the 
#inicial grades   
    if assignments==1:
        gradesFinal=grades   

#if more than one assignment start other operations                 
    if assignments>1:

#if there is a minimum, place 1 in the zeros matrix in the corresponding position
        for i in range (0,students):                    
            for j in range (0,assignments):             
                if grades[i,j]==np.min(grades[i,:]):
                    allzeros[i,j]=1                    


#to deal with duplicate minimums, if a 1 is found in the allzeros matrix,
#all other values are equal to 0
        for i in range (0,students):
            for j in range(0, assignments):             
                if allzeros[i,j]==1:
                    allzeros[i,j+1:]=0

#Remove the minimums by taking the inicial matrix where the allzeros matrix has 0's.
#Reshape the matrix so that everything does fine
        nomin=grades[allzeros==0]                       
        nomin=nomin.reshape(students,-1)

#If the 'nominimum' matrix has a -3, all of the grades of the student become a 
# -3     
        for i in range (0,students):
            for j in range (0,assignments):             
                if grades[i,j]==-3:
                    nomin[i,:]=-3

#Take the mean of the nominimums matrix, on the correct axis, and reshape it. 
        rawmean=nomin.mean(1)                           
        rawmean=rawmean.reshape(students,1)
             
# USE ROUNDGRADE TO GET FINAL GRADE       
        gradesFinal=roundGrade(rawmean)                

        return gradesFinal
        
