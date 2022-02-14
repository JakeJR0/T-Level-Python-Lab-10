import pandas as pd

dataframe = None

try:
  dataframe = pd.read_csv("baddata.csv")
except:
  pass

def show_data():
  print(dataframe.to_string())

def clean():
  global dataframe
  dataframe = dataframe.dropna() # This deletes any rows that have something missing in # the data set.
  show_data() # Shows the dataframe
  dataframe.dropna(inplace=True) # Deletes any rows that have something missing in the
  # data set.
  show_data() # Shows the dataframe
  dataframe.fillna(220, inplace=True) # This fills any column with missing data with
  # 220.
  show_data() # Shows the dataframe
  dataframe["Calories"].fillna(129, inplace=True) # This fills any missing data within
  # the calories column with 129.
  show_data() # Shows the dataframe

def clean_mean():
  x = dataframe["Calories"].mean() # Calculates the mean of the column.
  dataframe["Calories"].fillna(x, inplace=True) # This fills any missing data within
  # the calories column with the variable x.
  show_data() # Shows the dataframe
  

def clean_mode():
  x = dataframe["Calories"].mode()[0] # Calculates the mode of the column.
  dataframe["Calories"].fillna(x, inplace=True) # This fills any missing data within
  # the calories column with the variable x.
  show_data() # Shows the dataframe


def clean_median():
  x = dataframe["Calories"].median()[0] # Calculates the median of the column.
  dataframe["Calories"].fillna(x, inplace=True) # This fills any missing data within
  # the calories column with the variable x.
  show_data() # Shows the dataframe

def clean_format():
  dataframe["Date"] = pd.to_datetime(dataframe["Date"]) # Converts the column to a date.
  show_data() # Shows the dataframe
  dataframe["Date"] = pd.to_datetime(dataframe["Date"]) # Converts the column to a date.
  dataframe.dropna(subset=["Date"], inplace=True) # Removes any empty rows with an empty Date.
  show_data() # Shows the dataframe

def fix_data():
  dataframe.loc[7,'Duration'] = 45 # Sets row 7's Duration to 45.
  show_data() # Shows the dataframe


  for x in dataframe.index: # Loops through rows.
    if dataframe.loc[x, "Duration"] > 120: # Checks if the row's Duration is greater # than 120
      dataframe.loc[x, "Duration"] = 120 # Sets the row's Duration to 120
  show_data() # Shows the dataframe
    
  for x in dataframe.index:
    if dataframe.loc[x, "Duration"] > 120: # Checks if the row's Duration is greater # # than 120
      dataframe.drop(x, inplace = True) # Removes the row from the dataframe.
  show_data() # Shows the dataframe


def clean_duplicated():
  print(dataframe.duplicated()) # Shows the rows that are duplicated.
  dataframe.drop_duplicates(inplace=True) # Removes duplicated rows.
  show_data() # Shows the dataframe

show_data() # Shows the dataframe