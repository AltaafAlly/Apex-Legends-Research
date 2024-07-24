import pandas as pd

def merge_csv_files(file1, file2, output_file):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Concatenate the dataframes
    merged_df = pd.concat([df1, df2], ignore_index=True)
    
    # Save the merged dataframe to a new CSV file
    merged_df.to_csv(output_file, index=False)
    
    print(f"Files merged successfully into {output_file}")


merge_csv_files('Data_Retrieval/CSV_files/Uncleaned_data_PS.csv', 
                'Data_Retrieval/CSV_files/Uncleaned_data_Xbox.csv', 
                'Data_Retrieval/CSV_files/All_Player_Stats.csv')
