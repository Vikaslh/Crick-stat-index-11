# Crick-stat-index-11
this application help in pick the best playing 11 in cricket team with the give data 




Pandas  (KRISHNA KUMAR) week2 spent learning pandas.

why should we use pandas for our ml project?
is a powerful python library to organized the data and manipulate it to fix the discrepanies found in the collected data file .


how to integrate pandas with our machine learning model using pandas -

Pandas can be used to prepare and preprocess data for model training
and
to convert data into the format required by scikit learn library .




#getting started and install in vs code 

pip install pandas

#how to import it while it is required 

import pandas as pd




using it in our project because -



- to remove duplicate data 

df.drop_duplicates(inplace=True)




renaming the column according to our project needs 
for example to rename city to location.
df.rename(columns={'City': 'Location'}, inplace=True)

though we are collecting data from revelant sources , if the data file has missing details , can add it easily using the below code 
df['averageRunsScored'] = [100, 200,300]


how to group runs scored in different matches and take average of it 

grouped = df.groupby('matchtype')['runs'].mean()




creating and using data frames 

data frame is nothing but same as data structures in c language .

function to create data frame in pandas

dataFrameName = pd.DataFrame(dataVariablenName)



data inspection functions to use
df.head()   to display the first few rows of the dataframe.
df.tail()   to display the last few rowss of the data frame

df.info()       describes the datarame structure and gives insights into missing values . basically to get summary of the dataframe .
df.describe()  








how to select columns according to our need and perform operations on it 

#selecting a single column
NameOfVariable = df['columName']

#selecting multiple columns
subset = df[['wickets', 'sixes']]

#filtering rows based on a condition
variabeNameTostoreFilteredRows= df[df['runs'] < 50




              sorting the data 

df_sorted = df.sort_values(by='runsScored', ascending=False)
sorts in descending order since ascending=False , assign true for ascending order





                 can save the cleaned and structured data as csv or excel file .

df.to_csv('processedDataFilename.csv', index=False)







