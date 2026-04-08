from empty_verification import missing_values, column_variants
import pandas as pd

def pass_column_more_unique(df):
    """ This function takes a dataframe as input and returns the column names in a list which has more than 10 unique values"""
    unique_values=[]
    for column in df.columns:
        if df[column].nunique()>=10:
            unique_values.append(column) 
    return unique_values
    
df=pd.read_csv("C:\\Users\\HARIHARA SUTHAN\\Documents\\GitHub\\Loan-predictor-\\data\\raw\\train_data.csv")
missing_values(df)
column_variants(df,pass_column_more_unique(df))


    
if __name__ == "__main__":
    print("This is the main function of the program")