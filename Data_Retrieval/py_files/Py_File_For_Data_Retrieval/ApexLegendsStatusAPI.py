import requests
import csv
import time

# Replace with your actual API key
API_KEY = '22d0d035f3ebf343a5684221dc355c7f'

def get_player_stats(player_name, platform, version='5', enableClubsBeta=False, skipRank=False, merge=False, removeMerged=False):
    url = 'https://api.mozambiquehe.re/bridge'
    params = {
        'auth': API_KEY,
        'player': player_name,
        'platform': platform,
        'version': version
    }
    if enableClubsBeta:
        params['enableClubsBeta'] = 'true'
    if skipRank:
        params['skipRank'] = 'true'
    if merge:
        params['merge'] = 'true'
    if removeMerged:
        params['removeMerged'] = 'true'
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print('Failed to decode JSON response. Raw response:')
            print(response.text)
            return None
    else:
        print(f'Failed to access API. Status code: {response.status_code}')
        print('Raw response:')
        print(response.text)
        return None

def extract_relevant_stats(stats):
    relevant_stats = {'legends': {}, 'career': {}}
    legends = stats.get('legends', {}).get('all', {})
    global_stats = stats.get('legends', {}).get('all', {}).get('Global', {}).get('data', [])

    # Extract career stats
    for data in global_stats:
        key = data.get('key', '')
        if key in ['career_kills', 'career_revives', 'career_wins']:
            relevant_stats['career'][key] = data.get('value', 0)

    # Extract specified legend stats
    for legend, legend_data in legends.items():
        relevant_stats['legends'][legend] = {}
        for data in legend_data.get('data', []):
            name = data.get('name', '')
            if name in ['BR Kills', 'BR Damage', 'BR Wins']:
                relevant_stats['legends'][legend][name] = data.get('value', 0)

    return relevant_stats

def process_usernames_from_csv(input_csv, platform, output_csv, batch_size=100, wait_time=300):
    all_relevant_stats = []

    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        player_names = [row[0] for row in reader]  # Assuming the username is in the first column

    for i in range(0, len(player_names), batch_size):
        batch = player_names[i:i+batch_size]
        for player_name in batch:
            player_stats = get_player_stats(player_name, platform)
            if player_stats:
                relevant_stats = extract_relevant_stats(player_stats)
                relevant_stats['player_name'] = player_name  # Add player name to the stats
                all_relevant_stats.append(relevant_stats)
            print("Waiting 5 seconds to fetch next player's data...")
            time.sleep(5)  # Wait for 2 seconds between requests

        save_stats_to_csv(all_relevant_stats, output_csv)
        if i + batch_size < len(player_names):
            print(f"Batch {i//batch_size + 1} complete. Waiting {wait_time//60} minutes before next batch...")
            time.sleep(wait_time)  # Wait for the specified wait time before processing the next batch

def save_stats_to_csv(all_stats, filename):
    if not all_stats:
        print(f"No data to write to {filename}.")
        return

    headers = ['player_name', 'career_kills', 'career_wins', 'career_revives', 'legend', 'BR Kills', 'BR Damage', 'BR Wins']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        for stats in all_stats:
            player_name = stats.get('player_name', '')
            career_kills = stats.get('career', {}).get('career_kills', 0)
            career_wins = stats.get('career', {}).get('career_wins', 0)
            career_revives = stats.get('career', {}).get('career_revives', 0)
            
            if 'legends' in stats:
                for legend, legend_stats in stats['legends'].items():
                    row = [
                        player_name,
                        career_kills,
                        career_wins,
                        career_revives,
                        legend,
                        legend_stats.get('BR Kills', 0),
                        legend_stats.get('BR Damage', 0),
                        legend_stats.get('BR Wins', 0)
                    ]
                    writer.writerow(row)
            else:
                row = [
                    player_name,
                    career_kills,
                    career_wins,
                    career_revives,
                    '',
                    0,
                    0,
                    0
                ]
                writer.writerow(row)

    print(f"Player stats saved to {filename}")

# Example usage
input_csv = 'Data_Retrieval/CSV_files/usernames_for_Xbox_players.csv'  # CSV file containing the list of player usernames
platform = 'X1'  # Replace with the platform (PC, PS4, or X1)
output_csv = 'Data_Retrieval/CSV_files/Uncleaned_data_Xbox.csv'  # Output CSV file for storing the combined data

process_usernames_from_csv(input_csv, platform, output_csv)
