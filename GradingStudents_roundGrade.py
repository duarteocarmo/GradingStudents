#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:46:03 2017

@author: duarteocarmo
"""

#import relevant libraries and functions.
import numpy as np

#This function takes a vector with grades and rounds it to the nearest grade in 
#the 7 step scale. 
def roundGrade(grades):

#get the number of elements in the vector.
    classSize= np.size(grades)
    
    for i in range(0,classSize):     
#if element of vector satisfies condiction, give it a new value in the 
#7 step scale.
        if grades[i] <= -3:
            grades[i]=-3       
        if grades[i] > -3   and grades[i] < 1:      
            grades[i]=0                             
        if grades[i] >= 1   and grades[i] < 3:      
            grades[i]=2        
        if grades[i] >= 3   and grades[i] < 5.5:
            grades[i]=4        
        if grades[i] >= 5.5 and grades[i] < 8.5:
            grades[i]=7        
        if grades[i] >= 8.5 and grades[i] < 11:
            grades[i]=10        
        if grades[i] >= 11:
            grades[i]=12

#Return the rounded grades vector with the correct name            
    gradesRounded=np.array    
    gradesRounded=grades
    
    return gradesRounded