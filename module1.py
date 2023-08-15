import pandas as pd

# Function to read the CSV file into a DataFrame
def read_csv():
    file_path = "shopping.csv"
    df = pd.read_csv(file_path)
    #print(df.head())
    return df



# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    df = read_csv()
    df.duplicated().sum()
    return df




# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    df = check_duplicates()
    df.drop_duplicates(inplace=True)
    return df


# Function to check for null (missing) values in the DataFrame
def check_null_values():
    df = drop_duplicates()
    df.isnull().sum()
    return df



# Function to remove rows containing null values from the DataFrame
def remove_null_values():
    df = drop_duplicates()
    df.dropna(inplace=True)
    return df



# Function to rename specific columns in the DataFrame
def rename_columns():
    df = remove_null_values()
    print("DF before",df)
    column_name_map = {'reviews.text':'reviews_text',
                     'reviews.title':'reviews_title',
                     'reviews.date':'reviews_date'}
    df.rename(columns=column_name_map, inplace=True)
    print("DF after: ", df)
    return df

