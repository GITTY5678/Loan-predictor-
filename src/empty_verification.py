import pandas as pd

def missing_values(df):
    """ 
    This function has parameters of a csv file and then returns the number of missing values in each column
    it prints like this:
    Column name:number of missing values
    missing percentage : percentage of missing values in the column
    """
    missing_values_count=df.isnull().sum()
    missing_percentage=(missing_values_count/len(df))*100
    for column in df.columns:
        print(f"{column}:{missing_values_count[column]} missing values out of {len(df)} total values")
        print(f"missing percentage: {missing_percentage[column]:.2f}")
        print("----------------------------------------------------------------------")
        

def column_variants(df,columns=None):
    """
    This function takes a dataframe as input and returns the number of unique values in each column.
    It prints like this:
    Column name: number of unique values
    unique values : list of unique values in the column
    and also if columns are given as input then it will only return excluding that columns
    the columns parameter is a list of column names to be excluded from the analysis
    """
    if columns is not None:
        df = df[[col for col in df.columns if col not in columns]]
    for column in df.columns:
        unique_values=df[column].unique()
        print(f"{column}:{len(unique_values)} unique values")
        print(f"unique values: {unique_values}")
        print("----------------------------------------------------------------------")
