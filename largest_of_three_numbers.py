# -*- coding: utf-8 -*-
"""largest_of_three_numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lFmlIpTxxUwVx7DkkPGHqGA_fOm_f7GJ
"""

#pip install streamlit#

import streamlit as st
#import pandas as pd
#from sklearn import datasets
#from sklearn.ensemble import RandomForestClassifier
#import pickle

st.write("""
# LARGEST NUMBER AMONG THREE
""")

st.header('User Input Parameters')



num1 = float(st.input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
