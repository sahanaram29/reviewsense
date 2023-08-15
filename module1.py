import pandas as pd

# Function to read the CSV file into a DataFrame
def read_csv():
    # read the shopping.csv file using pandas library and return it
    file_path = "shopping.csv"
    df = pd.read_csv(file_path)
    #print(df.head())
    return df



# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    df.duplicated().sum()
    return df




# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # do not edit the predefined function name
    df = check_duplicates()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace=True)
    return df


# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # do not edit the predefined function name
    df = drop_duplicates()
    # Check for null values using the isnull() method and sum them for each column
    df.isnull().sum()
    return df



# Function to remove rows containing null values from the DataFrame
def remove_null_values():
    # do not edit the predefined function name
    df = drop_duplicates()
    # Drop rows containing null values using the dropna() method with inplace=True
    df.dropna(inplace=True)
    return df



# Function to rename specific columns in the DataFrame
def rename_columns():
    # do not edit the predefined function name
    df = remove_null_values()
    # Rename columns 'reviews.text', 'reviews.title', and 'reviews.date' to 'reviews_text', 'reviews_title', and 'reviews_date' respectively
    print("DF before",df)
    column_name_map = {'reviews.text':'reviews_text',
                     'reviews.title':'reviews_title',
                     'reviews.date':'reviews_date'}
    df.rename(columns=column_name_map, inplace=True)
    print("DF after: ", df)
    return df

