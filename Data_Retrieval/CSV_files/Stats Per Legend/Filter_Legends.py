import pandas as pd

# Load the CSV file into a pandas DataFrame
legend_stats = pd.read_csv('Data_Retrieval/CSV_files/Stats Per Legend/Legend_Stats_Transformed.csv')

# Define legend categories
legend_categories = {
    "Assault": ["Bangalore", "Fuse", "Ash", "Mad Maggie", "Ballistic"],
    "Skirmisher": ["Pathfinder", "Wraith", "Octane", "Revenant", "Horizon", "Valkyrie", "Alter"],
    "Recon": ["Bloodhound", "Crypto", "Seer", "Vantage"],
    "Support": ["Gibraltar", "Lifeline", "Mirage", "Loba", "Newcastle", "Conduit"],
    "Controller": ["Caustic", "Wattson", "Rampart", "Catalyst"]
}

# Function to determine the class of a legend
def classify_legend(legend_name):
    for category, legends in legend_categories.items():
        if legend_name in legends:
            return category
    return None

# Add a new column for the legend category
legend_stats['legend_category'] = legend_stats['legend'].apply(classify_legend)

# Filter out legends with all zero stats for each player
legend_stats_filtered = legend_stats[(legend_stats['BR Kills'] != 0) | 
                                     (legend_stats['BR Damage'] != 0) | 
                                     (legend_stats['BR Wins'] != 0)]

# Group by player and find the legend they use the most based on BR Kills, Damage, or Wins
# We assume the 'most used' is defined by the highest sum of these stats
legend_stats_filtered['total'] = legend_stats_filtered['BR Kills'] + \
                                 legend_stats_filtered['BR Damage'] + \
                                 legend_stats_filtered['BR Wins']

most_used_legends = legend_stats_filtered.sort_values('total', ascending=False).groupby('player_name').head(1)

# Drop the 'total' column used for sorting
most_used_legends.drop(columns=['total'], inplace=True)

# Save the filtered and categorized data to a new CSV file
most_used_legends.to_csv('filtered_legend_stats.csv', index=False)

print("Filtered legend stats have been saved to 'filtered_legend_stats.csv'")
