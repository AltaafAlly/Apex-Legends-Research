import pandas as pd

def separate_csv_files(input_file, output_file1, output_file2):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Select columns for the first output file
    df1 = df[['player_name', 'career_kills', 'career_wins', 'career_revives']].drop_duplicates()
    
    # Select columns for the second output file
    df2 = df[['player_name', 'legend', 'BR Kills', 'BR Damage', 'BR Wins']]
    
    # Ensure all relevant column values are stripped of any extra spaces
    df2.loc[:, 'legend'] = df2['legend'].str.strip()
    
    # Convert columns to numeric types
    df2['BR Kills'] = pd.to_numeric(df2['BR Kills'], errors='coerce')
    df2['BR Damage'] = pd.to_numeric(df2['BR Damage'], errors='coerce')
    df2['BR Wins'] = pd.to_numeric(df2['BR Wins'], errors='coerce')
    
    # Print the first few rows to ensure data is being read correctly
    print("First few rows of df2:")
    print(df2.head())
    
    # Print the data types of the columns
    print("Data types of df2:")
    print(df2.dtypes)
    
    # Print the rows to be removed for verification
    rows_to_remove = df2[(df2['legend'] == 'Global') & 
                         (df2['BR Kills'] == 0) & 
                         (df2['BR Damage'] == 0) & 
                         (df2['BR Wins'] == 0)]
    print("Rows to be removed:")
    print(rows_to_remove)
    
    # Drop rows where the stats match the criteria
    df2 = df2[~((df2['legend'] == 'Global') & 
                (df2['BR Kills'] == 0) & 
                (df2['BR Damage'] == 0) & 
                (df2['BR Wins'] == 0))]
    
    # Save the separated dataframes to new CSV files
    df1.to_csv(output_file1, index=False)
    df2.to_csv(output_file2, index=False)
    
    print(f"Data separated successfully into {output_file1} and {output_file2}")

# Replace 'input.csv', 'output1.csv', and 'output2.csv' with the paths to your CSV files
separate_csv_files('Data_Retrieval/CSV_files/Player Stats/Uncleaned Player Stats/PC/Uncleaned_data_PC.csv', 
                   'Data_Retrieval/Career_Stats_PC.csv', 
                   'Data_Retrieval/Legend_Stats_PC.csv')


# import pandas as pd

# def transform_legend_stats(input_file, output_file):
#     # Read the input CSV file
#     df = pd.read_csv(input_file)
    
#     # Pivot the data to make player_name unique with legends and their stats as columns
#     df_pivot = df.pivot_table(index='player_name', columns='legend', values=['BR Kills', 'BR Damage', 'BR Wins'], fill_value=0)
    
#     # Flatten the MultiIndex columns
#     df_pivot.columns = ['_'.join(col).strip() for col in df_pivot.columns.values]
    
#     # Reset the index to make player_name a column again
#     df_pivot.reset_index(inplace=True)
    
#     # Save the transformed dataframe to a new CSV file
#     df_pivot.to_csv(output_file, index=False)
    
#     print(f"Data transformed and saved successfully into {output_file}")

# # Replace 'input.csv' and 'output.csv' with the paths to your input and output CSV files
# transform_legend_stats('Data_Retrieval/CSV_files/Legend_Stats.csv', 
#                        'Data_Retrieval/CSV_files/Legend_Stats_Transformed.csv')


