# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:45:19 2021

@author: Shardul Kulkarni
"""

import os
import pandas as pd
import numpy as np
import re


class cheapest_operator_utility:
    
#########################################################################################            
# Function Name - generate_data
# Description   - Generate 'n' lists of operator with random prefixes and rates 
#                 (Made for data generation purpose only)
# Parameters    - 
#       n - Number of operator Lists to generate
# 
#########################################################################################

    def generate_data(n):
        data_path = os.getcwd() + '\\Data\\'
        try:
            os.mkdir(data_path)
        except:
            pass
            
        for opr in range(n):
            df = pd.DataFrame()
            np.random.seed(40+opr)
            df['prefix'] = pd.Series(np.random.randint(100,3000,5000))
            df['rate'] = pd.Series(np.random.uniform(0.1,10.0,5000)).round(2)
            df.prefix = df.prefix.apply(lambda x : str(x))
            df.to_csv(data_path + 'operator_'+str(opr+1)+'.csv',index=False)
    
    
#########################################################################################            
# Function Name - load_file
# Description   - Loads file from specified path
# Parameters    -  
#     file_name - Name of the file to be loaded
#     file_path - Path from where the file needs to be loaded
#########################################################################################

    def load_file(file_name,file_path):
        
        operator_name = os.path.splitext(file_name)[0]
        
        # Check if file is valid csv
        try:
            file_df = pd.read_csv(file_path+file_name)
            file_df.dropna(inplace = True)
        except:
            print('Skipping file : ',file_name,', as it is not a csv')
            return None , 0 
        
        file_df = file_df[[i for i in list(file_df.columns) if i in ['prefix','rate']]]

        # Check if csv is as per the required format
        if  ('prefix' not in list(file_df.columns)) | ('rate' not in list(file_df.columns)):
            print(file_name,'is not as per the format')
            return None , 0
        
        file_df['operator'] = operator_name
        
        return file_df , 1  

          
#########################################################################################            
# Function Name - pick_longest_matching_prefix
# Description   - From passed dataframe and number, the function calculates longest matching prefix
# Parameters    -  
#       file_df - Dataframe containing prefix and rate
#       numbr   - Inputted Phone no.  
#########################################################################################
    
    def pick_longest_matching_prefix(file_df,numbr):
        
        # Keeping just the numbers in prefix column
        file_df['prefix'] = file_df['prefix'].apply(lambda x : re.sub('\D', '', str(x)))
        
        # Flagging all prefixed in loaded file to inputted number
        file_df['flag'] = file_df['prefix'].apply(lambda x : np.where(re.search('^'+str(x), str(numbr)) == None , 0 ,1 ))
        
        # Calculating the length of the prefix
        file_df['len'] = file_df['prefix'].apply(lambda x : len(str(x)))
        
        # Filtering flagged prefixes, sorting them in descending order of length and picking the top prefix with respective rate
        file_df = file_df[(file_df['flag'] == 1)].sort_values(by=['len','rate'],ascending = [False,True]).head(1)
        return file_df[['prefix','rate','operator']]
 
    
#########################################################################################            
# Function Name - find_cheapest_operator
# Description   - Loads all the lists of operators from specified path and returns the 
#                 cheapest operator
# Parameters    -  
#       numbr   - Inputted Phone no.
#       path    - Path from where the files need to be loaded
#########################################################################################

    def find_cheapest_operator(numbr,path):
        
        if (re.search('[a-zA-Z]', str(numbr)) != None) | (re.search('[^a-zA-Z0-9]+', str(numbr)) != None) | (len(re.sub('\D', '', str(numbr))) != 12):
            return 'Invalid Phone Number'
        
        # Extract numbers from input numbr
        numbr = re.sub('\D', '', str(numbr))
        
        # Check the validty of the path
        try:
            dir_list = os.listdir(path)
        except:
            return 'Invalid Path'
        
        # Check if their are files in specified path
        if dir_list == []:
            return 'No files found'
        
        error_files = []
        tmp = pd.DataFrame()
        
        # Looping over list of files present in specified data path
        for file in dir_list:
                    
            opr_df, error_code = cheapest_operator_utility.load_file(file, path)
            
            if error_code != 1 :
                error_files.append(file)
                continue
                
            opr_df = cheapest_operator_utility.pick_longest_matching_prefix(opr_df, numbr)
            tmp = tmp.append(opr_df)
                
        # Check if all files are invalid
        if len(error_files) == len(dir_list):
            return 'All files are invalid'
        
        # Return operator name (if there is any)
        tmp = tmp.sort_values('rate',ascending=True).head(1)['operator'].reset_index(drop=True)
        if tmp.shape[0] == 0:
            return 'No operators available'
        else:
            return tmp[0]
  
# cheapest_operator_utility.generate_data(10)



