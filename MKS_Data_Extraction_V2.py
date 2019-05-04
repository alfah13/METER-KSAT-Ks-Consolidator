'''
This script reads in all csv files from the working directory and outputs a new
csv containing the name of the original file on the left, corresponding to 
the K normalized statement on the right
'''

import pandas as pd
import numpy as np
import os

#Create list of .csv files in my directory
files = [file for file in os.listdir( os.curdir ) if file.endswith(".csv")]  

#Initiate new list for holding tuples
new_data = []
for each_file in files: 
    
    #Import csv and convert to numpy matrix
    old_data = pd.read_csv(each_file).as_matrix() 
    
    #Index values in row 5 & 45 and add to container as tuple
    new_data += [(str(old_data[5][0]), str(old_data[45][0]))]


#Save as csv to the working directory with format "string"
np.savetxt('Your_New_CSV.csv', 
           new_data, 
           delimiter=',', 
           header = 'DATA FROM PREVIOUS CSVs:',
           fmt='%s')
