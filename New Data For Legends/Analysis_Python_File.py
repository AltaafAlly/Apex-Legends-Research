# %%
import pandas as pd
import os
import glob

# %%
# Define legend categories
legend_categories = {
    'Assault': ['Bangalore', 'Fuse', 'Ash', 'Mad Maggie', 'Ballistic'],
    'Skirmisher': ['Pathfinder', 'Wraith', 'Octane', 'Revenant', 'Horizon', 'Valkyrie','Alter'],
    'Recon': ['Bloodhound', 'Crypto', 'Seer', 'Vantage'],
    'Support': ['Gibraltar', 'Lifeline', 'Mirage', 'Loba', 'Newcastle', 'Conduit'],
    'Controller': ['Caustic', 'Wattson', 'Rampart', 'Catalyst']
}

# %%
# Flatten the dictionary to map legend to category
legend_to_category = {}
for category, legends in legend_categories.items():
    for legend in legends:
        legend_to_category[legend] = category


# %%
base_path = r'C:\Users\altaa\Documents\GitHub\Apex-Legends-Research\New Data For Legends'

damage_path = os.path.join(base_path, 'Legend Damage')
kills_path = os.path.join(base_path, 'Legend Kills')
matches_path = os.path.join(base_path, 'Legend Matches Played')
wins_path = os.path.join(base_path, 'Legend Wins')
# Function to list files in a directory
def list_files(directory):
    print(f"Files in {directory}:")
    for f in os.listdir(directory):
        print(f)

# List files in each directory
list_files(damage_path)
list_files(kills_path)
list_files(matches_path)
list_files(wins_path)

# %%
# Initialize an empty list to hold dataframes for each legend
legend_dataframes = []

# Get list of legends
legends = list(legend_to_category.keys())

# %%
#Loop over each legend
for legend in legends:
    try:
        # Build file paths for the legend
        legend_damage_file = os.path.join(damage_path, f"{legend}_damage.csv")
        legend_kills_file = os.path.join(kills_path, f"{legend}_kills.csv")
        legend_matches_file = os.path.join(matches_path, f"{legend}_games_played.csv")  # Updated suffix
        legend_wins_file = os.path.join(wins_path, f"{legend}_wins.csv")
        
        # Check if all files exist
        required_files = [legend_damage_file, legend_kills_file, legend_matches_file, legend_wins_file]
        missing_files = [f for f in required_files if not os.path.exists(f)]
        if missing_files:
            print(f"Data files for legend '{legend}' are missing: {missing_files}. Skipping this legend.")
            continue  # Skip to the next legend if any file is missing
        
        # Read the data files
        df_damage = pd.read_csv(legend_damage_file, header=None, names=['Damage'], skiprows=1)
        df_matches = pd.read_csv(legend_matches_file, header=None, names=['Games Played'], skiprows=1)
        df_wins = pd.read_csv(legend_wins_file, header=None, names=['Wins'], skiprows=1)

        # Custom converter to handle numeric values and ignore non-numeric ones
        def convert_number(s):
            try:
                # Remove commas and quotes, then convert to integer
                return int(str(s).replace(',', '').replace('"', '').strip())
            except ValueError:
                # Return NaN if conversion fails
                return pd.NA

        # Read the kills CSV file with the custom converter
        df_kills = pd.read_csv(legend_kills_file, header=None, names=['Kills'], converters={0: convert_number}, skiprows=1)

        # Combine the data into a single DataFrame, aligning on index (axis=1)
        df_legend = pd.concat([df_damage.reset_index(drop=True), 
                               df_kills.reset_index(drop=True), 
                               df_matches.reset_index(drop=True), 
                               df_wins.reset_index(drop=True)], axis=1)

        # Add 'legend_name' column to identify the legend in the combined DataFrame
        df_legend['legend_name'] = legend

        # Append the processed DataFrame to the list
        legend_dataframes.append(df_legend)
    
    except Exception as e:
        # Catch any exceptions during processing and print the error
        print(f"An error occurred while processing legend '{legend}': {e}")

# %%
# Concatenate all legend dataframes
all_legends_df = pd.concat(legend_dataframes, ignore_index=True)

# Map legends to categories
all_legends_df['Legend_Category'] = all_legends_df['legend_name'].map(legend_to_category)

all_legends_df

# %%
# Ensure that columns are numeric, forcing invalid values to NaN
all_legends_df['Kills'] = pd.to_numeric(all_legends_df['Kills'], errors='coerce')
all_legends_df['Wins'] = pd.to_numeric(all_legends_df['Wins'], errors='coerce')
all_legends_df['Games Played'] = pd.to_numeric(all_legends_df['Games Played'], errors='coerce')
all_legends_df['Damage'] = pd.to_numeric(all_legends_df['Damage'], errors='coerce')

# Avoid division by zero and handle NaN
all_legends_df['Kills_per_Win'] = all_legends_df.apply(lambda row: row['Kills'] / row['Wins'] if pd.notna(row['Wins']) and row['Wins'] > 0 else 0, axis=1)
all_legends_df['Kills_per_Match'] = all_legends_df.apply(lambda row: row['Kills'] / row['Games Played'] if pd.notna(row['Games Played']) and row['Games Played'] > 0 else 0, axis=1)
all_legends_df['Damage_per_Match'] = all_legends_df.apply(lambda row: row['Damage'] / row['Games Played'] if pd.notna(row['Games Played']) and row['Games Played'] > 0 else 0, axis=1)

# Group by 'Legend_Category' and calculate the mean of the relevant columns
averaged_stats_df = all_legends_df.groupby('Legend_Category').agg(
    Average_Kills_per_Win=('Kills_per_Win', 'mean'),
    Average_Kills_per_Match=('Kills_per_Match', 'mean'),
    Average_Damage_per_Match=('Damage_per_Match', 'mean')
).reset_index()

# Display the aggregated statistics
print(averaged_stats_df)

# %% [markdown]
# # When it comes to wins Alter, Ballistic, Conduit and Newcastle do not have data of their wins. So we can't use them to calculate the win rate.

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Plot 1: Average Kills per Win by Legend Category
plt.figure(figsize=(10, 6))
sns.barplot(x='Legend_Category', y='Average_Kills_per_Win', data=averaged_stats_df, palette='Blues_d')
plt.title('Average Kills per Win by Legend Category')
plt.xlabel('Legend Category')
plt.ylabel('Average Kills per Win')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 2: Average Kills per Match by Legend Category
plt.figure(figsize=(10, 6))
sns.barplot(x='Legend_Category', y='Average_Kills_per_Match', data=averaged_stats_df, palette='Oranges_d')
plt.title('Average Kills per Match by Legend Category')
plt.xlabel('Legend Category')
plt.ylabel('Average Kills per Match')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 3: Average Damage per Match by Legend Category
plt.figure(figsize=(10, 6))
sns.barplot(x='Legend_Category', y='Average_Damage_per_Match', data=averaged_stats_df, palette='Greens_d')
plt.title('Average Damage per Match by Legend Category')
plt.xlabel('Legend Category')
plt.ylabel('Average Damage per Match')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# %% [markdown]
# # ANOVA (Analysis of Variance)

# %%
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ANOVA for Kills per Match
groups_kpm = [group['Kills_per_Match'].dropna().values for name, group in all_legends_df.groupby('Legend_Category')]
f_stat_kpm, p_val_kpm = stats.f_oneway(*groups_kpm)
print(f"ANOVA for Kills per Match: F-statistic={f_stat_kpm}, p-value={p_val_kpm}")

# ANOVA for Kills per Win
groups_kpw = [group['Kills_per_Win'].dropna().values for name, group in all_legends_df.groupby('Legend_Category')]
f_stat_kpw, p_val_kpw = stats.f_oneway(*groups_kpw)
print(f"ANOVA for Kills per Win: F-statistic={f_stat_kpw}, p-value={p_val_kpw}")


# %% [markdown]
# # Post-hoc Tests (Tukey’s HSD)

# %%
# Tukey's HSD for Kills per Match
tukey_kpm = pairwise_tukeyhsd(endog=all_legends_df['Kills_per_Match'].dropna(),
                             groups=all_legends_df['Legend_Category'].dropna(),
                             alpha=0.05)
print(tukey_kpm)

# Tukey's HSD for Kills per Win
tukey_kpw = pairwise_tukeyhsd(endog=all_legends_df['Kills_per_Win'].dropna(),
                             groups=all_legends_df['Legend_Category'].dropna(),
                             alpha=0.05)
print(tukey_kpw)


# %% [markdown]
# # Assumption Checks:
# 
# # Normality:
# 
# # Use Shapiro-Wilk test or Q-Q plots to assess normality

# %%
from scipy.stats import shapiro

# Shapiro-Wilk Test for Kills per Match
stat_kpm, p_kpm = shapiro(all_legends_df['Kills_per_Match'].dropna())
print(f"Shapiro-Wilk Test for Kills per Match: Stat={stat_kpm}, p-value={p_kpm}")

# Shapiro-Wilk Test for Kills per Win
stat_kpw, p_kpw = shapiro(all_legends_df['Kills_per_Win'].dropna())
print(f"Shapiro-Wilk Test for Kills per Win: Stat={stat_kpw}, p-value={p_kpw}")


# %% [markdown]
# # Levene’s Test for Homogeneity of Variances:

# %%
from scipy.stats import levene

# Levene’s Test for Kills per Match
stat_levene_kpm, p_levene_kpm = levene(*groups_kpm)
print(f"Levene’s Test for Kills per Match: Stat={stat_levene_kpm}, p-value={p_levene_kpm}")

# Levene’s Test for Kills per Win
stat_levene_kpw, p_levene_kpw = levene(*groups_kpw)
print(f"Levene’s Test for Kills per Win: Stat={stat_levene_kpw}, p-value={p_levene_kpw}")


# %% [markdown]
# # Handling Violations

# %%
from scipy.stats import kruskal

# Kruskal-Wallis Test for Kills per Match
stat_kw_kpm, p_kw_kpm = kruskal(*groups_kpm)
print(f"Kruskal-Wallis Test for Kills per Match: Stat={stat_kw_kpm}, p-value={p_kw_kpm}")

# Kruskal-Wallis Test for Kills per Win
stat_kw_kpw, p_kw_kpw = kruskal(*groups_kpw)
print(f"Kruskal-Wallis Test for Kills per Win: Stat={stat_kw_kpw}, p-value={p_kw_kpw}")


# %% [markdown]
# # Implementing Unsupervised Learning: Clustering

# %%
clustering_data = all_legends_df[['Kills_per_Match', 'Damage_per_Match', 'Kills_per_Win']].dropna()


# %%
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustering_data)


# %%
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()


# %%
from sklearn.metrics import silhouette_score

silhouette_scores = []
K = range(2, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(scaled_data)
    silhouette_avg = silhouette_score(scaled_data, cluster_labels)
    silhouette_scores.append(silhouette_avg)
    print(f"For n_clusters = {k}, the average silhouette_score is : {silhouette_avg}")

# Plot Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(K, silhouette_scores, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Method for Optimal k')
plt.show()


# %%
# Fit K-Means with optimal k
optimal_k = 5  # Replace with your chosen k based on Elbow and Silhouette methods
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add cluster labels to the DataFrame
clustering_data['Cluster'] = clusters


# %%
import seaborn as sns

sns.pairplot(clustering_data, vars=['Kills_per_Match', 'Damage_per_Match', 'Kills_per_Win'], hue='Cluster', palette='Set1')
plt.show()


# %%
# Inverse transform to original scale
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=['Kills_per_Match', 'Damage_per_Match', 'Kills_per_Win'])
cluster_centers_df['Cluster'] = range(optimal_k)
print(cluster_centers_df)


# %%
# Add Cluster labels to the main DataFrame
all_legends_df = all_legends_df.loc[clustering_data.index]
all_legends_df['Cluster'] = clusters

plt.figure(figsize=(12, 6))
sns.countplot(x='Legend_Category', hue='Cluster', data=all_legends_df, palette='Set2')
plt.title('Legend Category Distribution Across Clusters')
plt.xlabel('Legend Category')
plt.ylabel('Count')
plt.legend(title='Cluster')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# %%
all_legends_df

# %% [markdown]
# # Stats per Legend

# %%
import matplotlib.pyplot as plt

# Group the dataframe by 'legend_name' and sum total Kills, Wins, Games Played, and Damage for each legend
legend_stats_df = all_legends_df.groupby('legend_name').agg(
    Total_Kills=('Kills', 'sum'),
    Total_Wins=('Wins', 'sum'),
    Total_Games_Played=('Games Played', 'sum'),
    Total_Damage=('Damage', 'sum')
).reset_index()

# Calculate Kills per Win
legend_stats_df['Kills_per_Win'] = legend_stats_df['Total_Kills'] / legend_stats_df['Total_Wins']

# Calculate a weighted Kills per Win, weighting by games played
legend_stats_df['Weighted_Kills_per_Win'] = legend_stats_df['Kills_per_Win'] * (legend_stats_df['Total_Games_Played'] / legend_stats_df['Total_Games_Played'].max())

# Calculate Kills per Match
legend_stats_df['Kills_per_Match'] = legend_stats_df['Total_Kills'] / legend_stats_df['Total_Games_Played']

# Calculate Damage per Match
legend_stats_df['Damage_per_Match'] = legend_stats_df['Total_Damage'] / legend_stats_df['Total_Games_Played']

# Calculate weighted Kills per Match
legend_stats_df['Weighted_Kills_per_Match'] = legend_stats_df['Kills_per_Match'] * (legend_stats_df['Total_Games_Played'] / legend_stats_df['Total_Games_Played'].max())

# Calculate weighted Damage per Match
legend_stats_df['Weighted_Damage_per_Match'] = legend_stats_df['Damage_per_Match'] * (legend_stats_df['Total_Games_Played'] / legend_stats_df['Total_Games_Played'].max())

# Sort by Weighted Kills per Win and plot
sorted_by_weighted_kills_per_win = legend_stats_df.sort_values(by='Weighted_Kills_per_Win', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(sorted_by_weighted_kills_per_win['legend_name'], sorted_by_weighted_kills_per_win['Weighted_Kills_per_Win'], color='skyblue')
plt.title('Weighted Kills per Win by Legend (Descending Order)')
plt.xlabel('Legend')
plt.ylabel('Weighted Kills per Win')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Sort by Weighted Kills per Match and plot (Fixed sorting issue)
sorted_by_weighted_kills_per_match = legend_stats_df.sort_values(by='Weighted_Kills_per_Match', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(sorted_by_weighted_kills_per_match['legend_name'], sorted_by_weighted_kills_per_match['Weighted_Kills_per_Match'], color='orange')
plt.title('Weighted Kills per Match by Legend (Descending Order)')
plt.xlabel('Legend')
plt.ylabel('Weighted Kills per Match')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Sort by Weighted Damage per Match and plot
sorted_by_weighted_damage_per_match = legend_stats_df.sort_values(by='Weighted_Damage_per_Match', ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(sorted_by_weighted_damage_per_match['legend_name'], sorted_by_weighted_damage_per_match['Weighted_Damage_per_Match'], color='green')
plt.title('Weighted Damage per Match by Legend (Descending Order)')
plt.xlabel('Legend')
plt.ylabel('Weighted Damage per Match')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# %%



