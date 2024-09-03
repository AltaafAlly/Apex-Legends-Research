# import pandas as pd

# # Load the CSV file into a pandas DataFrame
# legend_stats = pd.read_csv('Data_Retrieval/CSV_files/Stats Per Legend/Legend_Stats_Transformed.csv')

# # Define legend categories
# legend_categories = {
#     "Assault": ["Bangalore", "Fuse", "Ash", "Mad Maggie", "Ballistic"],
#     "Skirmisher": ["Pathfinder", "Wraith", "Octane", "Revenant", "Horizon", "Valkyrie", "Alter"],
#     "Recon": ["Bloodhound", "Crypto", "Seer", "Vantage"],
#     "Support": ["Gibraltar", "Lifeline", "Mirage", "Loba", "Newcastle", "Conduit"],
#     "Controller": ["Caustic", "Wattson", "Rampart", "Catalyst"]
# }

# # Function to determine the class of a legend
# def classify_legend(legend_name):
#     for category, legends in legend_categories.items():
#         if legend_name in legends:
#             return category
#     return None

# # Add a new column for the legend category
# legend_stats['legend_category'] = legend_stats['legend'].apply(classify_legend)

# # Filter out legends with all zero stats for each player
# legend_stats_filtered = legend_stats[(legend_stats['BR Kills'] != 0) | 
#                                      (legend_stats['BR Damage'] != 0) | 
#                                      (legend_stats['BR Wins'] != 0)]

# # Group by player and find the legend they use the most based on BR Kills, Damage, or Wins
# # We assume the 'most used' is defined by the highest sum of these stats
# legend_stats_filtered['total'] = legend_stats_filtered['BR Kills'] + \
#                                  legend_stats_filtered['BR Damage'] + \
#                                  legend_stats_filtered['BR Wins']

# most_used_legends = legend_stats_filtered.sort_values('total', ascending=False).groupby('player_name').head(1)

# # Drop the 'total' column used for sorting
# most_used_legends.drop(columns=['total'], inplace=True)

# # Save the filtered and categorized data to a new CSV file
# most_used_legends.to_csv('filtered_legend_stats.csv', index=False)

# print("Filtered legend stats have been saved to 'filtered_legend_stats.csv'")


import pandas as pd

# Define legend categories
legend_categories = {
    'Assault': ['Bangalore', 'Fuse', 'Ash', 'Mad Maggie', 'Ballistic'],
    'Skirmisher': ['Pathfinder', 'Wraith', 'Octane', 'Revenant', 'Horizon', 'Valkyrie', 'Alter'],
    'Recon': ['Bloodhound', 'Crypto', 'Seer', 'Vantage'],
    'Support': ['Gibraltar', 'Lifeline', 'Mirage', 'Loba', 'Newcastle', 'Conduit'],
    'Controller': ['Caustic', 'Wattson', 'Rampart', 'Catalyst']
}

# Function to categorize legends
def categorize_legend(legend):
    for category, legends in legend_categories.items():
        if legend in legends:
            return category
    return 'Unknown'  # In case a legend does not fit into any category

# Function to categorize legends in a dataset
def categorize_legends_in_dataset(file_path, output_path):
    # Read the CSV file into a DataFrame
    legend_stats_df = pd.read_csv(file_path)

    # Add a new column 'legend_category' based on the legend's name
    legend_stats_df['legend_category'] = legend_stats_df['legend'].apply(categorize_legend)

    # Save the updated DataFrame to a new CSV file
    legend_stats_df.to_csv(output_path, index=False)
    print(f"Categorized legend stats saved to {output_path}")

# Paths to the input and output CSV files for each platform
paths = {
    "PC": {
        "input": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Player Stats\Cleaned Player Stats\Legend Stats\Legend_Stats_PC.csv",
        "output": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Stats Per Legend\Legend_Stats_PC_Categorized.csv"
    },
    "PS4": {
        "input": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Player Stats\Cleaned Player Stats\Legend Stats\Legend_Stats_PS4.csv",
        "output": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Stats Per Legend\Legend_Stats_PS4_Categorized.csv"
    },
    "Xbox": {
        "input": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Player Stats\Cleaned Player Stats\Legend Stats\Legend_Stats_Xbox.csv",
        "output": r"C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\Data_Retrieval\CSV_files\Stats Per Legend\Legend_Stats_Xbox_Categorized.csv"
    }
}

# Apply the categorization to each platform's dataset
for platform, paths_dict in paths.items():
    print(f"Processing {platform} dataset...")
    categorize_legends_in_dataset(paths_dict["input"], paths_dict["output"])

print("Legend categorization completed for all platforms.")
