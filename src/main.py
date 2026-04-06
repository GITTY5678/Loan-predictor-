from empty_verification import missing_values, column_variants
import pandas as pd

df=pd.read_csv("C:\\Users\\HARIHARA SUTHAN\\Documents\\GitHub\\Loan-predictor-\\data\\raw\\train_data.csv")
missing_values(df)
column_variants(df)

if __name__ == "__main__":
    print("This is the main function of the program")
    