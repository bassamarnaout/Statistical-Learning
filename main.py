# Python Project Template

import numpy as np

outputString = []

'''**********************************************************************************************
FUNCTIONS
**********************************************************************************************'''
def write_to_file(text):
    # write data in a file.
    file = open("results.txt", "a")
    file.writelines('\n')
    file.writelines(text)
    file.close()

'''**********************************************************************************************
END OF FUNCTIONS
**********************************************************************************************'''



'''**********************************************************************************************
1. Prepare Problem'
**********************************************************************************************'''
# a) Load libraries
import pandas as pd

# b) Load dataset // Load Machine Learning Data
data = pd.read_csv('HCV-Egy-Data.csv')
# outputString.append('Shape of Data:')
outputString.append(str(data.shape))


'''**********************************************************************************************
2. Summarize Data
**********************************************************************************************'''
# a) Descriptive statistics

# a1.Take a peek at your raw data.
# a2.Review the dimensions of your dataset.
# a3.Review the data types of attributes in your data.
# a4.Summarize the distribution of instances across classes in your dataset.
# a5.Summarize your data using descriptive statistics.
# a6.Understand the relationships in your data using correlations.
# a7.Review the skew of the distributions of each attribute.


# a1.Take a peek at your raw data.
#review the first 20 rows
# outputString.append(data.head(20))
# data.head(20)

x =  data.head(20)
outputString.append(x.iloc[:4, :10])
# outputString.append(x[:10,:10])
# b) D ata visualizations









# 3. Prepare Data
# a) Data Cleaning
# b) Feature Selection
# c) Data Transforms
# 4. Evaluate Algorithms
# a) Split-out validation dataset
# b) Test options and evaluation metric
# c) Spot Check Algorithms
# d) Compare Algorithms
# 5. Improve Accuracy
# a) Algorithm Tuning
# b) Ensembles
# 6. Finalize Model
# a) Predictions on validation dataset
# b) Create standalone model on entire training dataset
# c) Save model for later use




# print and output to txt file.
outputString.append('\n\n')
# write data in a file.
file = open("results.txt", "w") # to delete the content of the file
file.close()


for str_ in outputString:
    print(str_)
    write_to_file(str_)


print('*'*60)
print('PLEASE CHECK "results.txt"  FOR GENERATED OUTPUT...')
print('*'*60)

'''**********************************************************************************************
END 
**********************************************************************************************'''