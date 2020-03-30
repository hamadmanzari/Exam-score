# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 07:54:49 2020

@author: hamad
"""
while True:   
    x = input("Enter exam score\n")
    if x == "exit":
        break
    if int(x) >= 67:
        print("Congratlations!!!")
        print("You have passed the exam")
    else:
        print("Sorry")
        print("You have failed the exam")
        

